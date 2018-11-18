import concurrent.futures
import math
import re
import time
from lp_api_wrapper.parsers import Conversations
from lp_api_wrapper.util.wrapper_base import WrapperBase, APIMethod


class MessagingInteractions(WrapperBase):
    """
    Python Wrapper for the LivePerson Messaging Interactions API

    Documentation:
    https://developers.liveperson.com/data-messaging-interactions-overview.html
    """

    def __init__(self, auth,version="1", company=None, source="LPApiWrapper"):

        super().__init__(auth=auth)

        # Establish Base URL
        domain = self.get_domain(account_id=auth.account_id, service_name='msgHist')
        self.base_url = 'https://{}/messaging_history/api/account/{}/conversations'.format(domain, auth.account_id)
        self.version = version
        self.company = company
        self.source = source

    def conversations(self, body, offset=0, limit=100, sort=None):
        """
        Documentation:
        https://developers.liveperson.com/data_api-messaging-interactions-conversations.html

        * Returns a single offset of data within start time range *

        :param body: dict <Required>
        :param offset: int
        :param limit: int
        :param sort: str
        :return Decoded JSON data
        """
        num_retries = 3
        error = True
        wait_time = 30
        for trial in range(1,num_retries):
            if(error):
                try:
                    api_return = self.process_request(
                        method=APIMethod.POST,
                        url='{}/search'.format(self.base_url),
                        url_parameters={
                            'offset': offset,
                            'limit': limit,
                            'sort': sort,
                            'v':self.version,
                            'company':self.company,
                            'source':self.source
                        },
                        body=body
                    )
                    error = False
                    return api_return
                except Exception:
                    time.sleep(trial * wait_time)

    def all_conversations(self, body, max_workers=7, debug=0, parse_data=False, offset=0, max_limit=None):
        """
        Documentation:
        https://developers.liveperson.com/data_api-messaging-interactions-conversations.html

        * Returns all offsets of data within start time range *

        :param body: dict <Required>
        :param max_workers: int (Max # of concurrent requests)
        :param debug: int (Status of API requests: 1=full, 2=summary, default=0)
        :param parse_data: bool (Returns a parsed Engagements data object.)
        :param offset: Start offset
        :param max_limit: Max conversations to retrieve. Default -1, is all conversations based on the body
        :return List of conversations history records as decoded JSON data
        """

        # Grab first offset of data.
        initial_data = self.conversations(body=body, offset=offset)

        # Number of conversations in date range that was selected in the body start parameters.
        count = initial_data['_metadata']['count']

        # Max number of retrivals per call
        limit = 100
        offset_start = offset
        # Total number of conversation to actually retrieve
        if(max_limit is None):
            total_conversation = count - offset
            last_conversation = count
        else:
            if(count > max_limit + offset):
                total_conversation = max_limit
                last_conversation = max_limit + offset
            else:
                total_conversation = count - offset
                last_conversation = count

        # Retrieve site ID from URL
        lesite = re.search('account/(.*)/conversations', self.base_url)
        lesite = lesite.group(1)

        # If there are no conversations in data range, return nothing.
        if count == 0:
            if debug == 1:
                print('[MIAPI Status]: There are 0 records!')
            return None
        else:
            if debug >= 1:
                print('[MIAPI Summary]: count=%s reqs=%s workers=%s leSite=%s' % (total_conversation, math.ceil(total_conversation/limit), max_workers, lesite))

        # Set up delivery options.
        conversations = Conversations() if parse_data else []

        # Multi-threading to handle multiple requests at a time.
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:

            future_requests = {}
            last_call = False
            while(not last_call):
                if(offset_start + limit >= last_conversation):
                    limit = last_conversation - offset_start
                    future_requests[executor.submit(self.conversations, body, offset_start, limit)] = offset_start
                    last_call = True
                else:
                    future_requests[executor.submit(self.conversations, body, offset_start, limit)] = offset_start
                    offset_start = offset_start + limit

            for future in concurrent.futures.as_completed(future_requests):
                if debug == 1:
                    print('[MIAPI Offset Status]: {} of {} records completed!'.format(future_requests[future] - offset, total_conversation ))

                # Grab dict with 'conversationHistoryRecords' from the request.  Removing any '_metadata' info.
                records = future.result()['conversationHistoryRecords']

                # Store results.
                if parse_data:
                    conversations.append_records(records=[record for record in records])
                else:
                    conversations.extend([record for record in records])

        return conversations

    def all_conversations_full(self, body, max_workers=7, debug=0, parse_data=False):
        conversations = self.all_conversations(body, max_workers=max_workers, debug=debug, parse_data=parse_data)
        partial_conversations =set([])
        if(conversations is not None):
            # Step 1) Remove all the conversations that are partial
            if(parse_data == True):
                for conv in conversations.info:
                    if(conv.isPartial):
                        partial_conversations.add(conv.conversationId)
                #E.g: events = ['agent_participants', 'campaign', 'cobrowse_sessions', 'consumer_participants', 'conversation_surveys', 'customer_info', 'info',.......]
                events = [a for a in dir(conversations) if not a.startswith('__') and not callable(getattr(conversations, a)) and isinstance(getattr(conversations, a), list)]
                for ev in events:
                    list_event = getattr(conversations, ev)
                    full_event = [x for x in list_event if x.conversationId not in partial_conversations]
                    setattr(conversations, ev, full_event)
            else:
                for conv in conversations:
                    if(conv['info']['isPartial'] == True):
                        partial_conversations.add(conv['info']['conversationId'])
                conversations = [x for x in conversations if x['info']['conversationId'] not in partial_conversations]
            # Step 2) Retrieve the conversations that were partial again but individually
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                # Create all future requests for the conversations that were originally partially complete.
                future_requests = {
                    executor.submit(self.get_conversation_by_conversation_id, conversation_id) : conversation_id for conversation_id in partial_conversations
                }
                for future in concurrent.futures.as_completed(future_requests):
                    records = future.result()['conversationHistoryRecords']
                    if (parse_data == True):
                        conversations.append_records(records=[record for record in records])
                    else:
                        conversations.extend([record for record in records])

        return conversations

    def all_conversations_by_chunks(self, body, max_workers=7, debug=0, parse_data=False):
        """
        Documentation:
        https://developers.liveperson.com/data_api-messaging-interactions-conversations.html

        * Returns all offsets of data within start time range *

        :param body: dict <Required>
        :param max_workers: int (Max # of concurrent requests)
        :param debug: int (Status of API requests: 1=full, 2=summary, default=0)
        :param parse_data: bool (Returns a parsed Engagements data object.)
        :return List of conversations history records as decoded JSON data
        """

        # Grab first offset of data.
        initial_data = self.conversations(body=body, offset=0)

        # Number of conversations in date range that was selected in the body start parameters.
        count = initial_data['_metadata']['count']

        # Retrieve site ID from URL
        lesite = re.search('account/(.*)/conversations', self.base_url)
        lesite = lesite.group(1)

        # Max number of retrivals per call
        limit_per_call = 100

        # If there are no conversations in data range, return nothing.
        if count == 0:
            if debug == 1:
                print('[MIAPI Status]: There are 0 records!')
            return None
        else:
            if debug >= 1:
                print('[MIAPI Summary]: count=%s reqs=%s workers=%s leSite=%s' % (count, math.ceil(count/limit_per_call), max_workers, lesite))
            chunk_size = 500 # MUST be greater than the limit_per_call
            chunk_offset = 0
            offset = 0
            chunks = math.ceil(count/chunk_size)

        # E.g Count =468, chunk_size =150 then chunks 4
        # Will iterate 4 times
        for iterat in range(1, chunks + 1):
            conversations = Conversations() if parse_data else []
            future_requests = {}
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:

                # First iteration: chunk_offset =0 , chunk_offset + chunk_size = 150 , limit_per_call=100,  list_offset = [0,100]
                # Second iteration:  chunk_offset =150 , chunk_offset + chunk_size = 300 , limit_per_call=100,  list_offset = [150,250]
                # Fourth iteration: list_offset = [450,600]
                list_offset = range(chunk_offset, chunk_offset + chunk_size, limit_per_call)
                for elem in list_offset:
                    if(elem < count): # If the element is greater than the total count, we dont need to make a call starting with that offset
                        if (elem + limit_per_call > chunk_offset + chunk_size):  # For second iteration, second element: 250 + 100 > 150 + 150; For fourth iteration, second element: won't pass previous if
                            limit_per_call = chunk_size - limit_per_call # 150 - 100 = 50 
                        future_requests[executor.submit(self.conversations, body, offset, limit_per_call)] = offset
                        offset = offset + limit_per_call


                for future in concurrent.futures.as_completed(future_requests):

                    if debug == 1:
                        print('[MIAPI Offset Status]: {} of {} records completed!'.format(future_requests[future], count))

                    # Grab dict with 'conversationHistoryRecords' from the request.  Removing any '_metadata' info.
                    records = future.result()['conversationHistoryRecords']

                    # Store results.
                    if parse_data:
                        conversations.append_records(records=[record for record in records])
                    else:
                        conversations.extend([record for record in records])

                limit_per_call = 100
                chunk_offset = chunk_offset + chunk_size
            yield conversations

    def get_conversation_by_conversation_id(self, conversation_id):
        """
        Documentation:
        https://developers.liveperson.com/data_api-messaging-interactions-get-conversation-by-conversation-id.html

        :param conversation_id: str <Required>
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.POST,
            url='{}/conversation/search'.format(self.base_url),
            body={
                'conversationId': conversation_id
            }
        )

    def get_conversations_by_consumer_id(self, consumer_id, status=None):
        """
        Documentation:
        https://developers.liveperson.com/data_api-messaging-interactions-get-conversations-by-consumer-id.html

        :param consumer_id: str <Required>
        :param status: List[str]
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.POST,
            url='{}/consumer/search'.format(self.base_url),
            body={
                'consumer': consumer_id,
                'status': status
            }
        )
