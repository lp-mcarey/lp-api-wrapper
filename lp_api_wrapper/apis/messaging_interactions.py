import concurrent.futures
import math
import re
from lp_api_wrapper.parsers import Conversations
from lp_api_wrapper.util.wrapper_base import WrapperBase, APIMethod


class MessagingInteractions(WrapperBase):
    """
    Python Wrapper for the LivePerson Messaging Interactions API

    Documentation:
    https://developers.liveperson.com/data-messaging-interactions-overview.html
    """

    def __init__(self, auth):

        super().__init__(auth=auth)

        # Establish Base URL
        domain = self.get_domain(account_id=auth.account_id, service_name='msgHist')
        self.base_url = 'https://{}/messaging_history/api/account/{}/conversations'.format(domain, auth.account_id)

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

        return self.process_request(
            method=APIMethod.POST,
            url='{}/search'.format(self.base_url),
            url_parameters={
                'offset': offset,
                'limit': limit,
                'sort': sort
            },
            body=body
        )

    def all_conversations(self, body, max_workers=7, debug=0, parse_data=False):
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
        limit = 100

        # If there are no conversations in data range, return nothing.
        if count == 0:
            if debug == 1:
                print('[MIAPI Status]: There are 0 records!')
            return None
        else:
            if debug >= 1:
                print('[MIAPI Summary]: count=%s reqs=%s workers=%s leSite=%s' % (count, math.ceil(count/limit), max_workers, lesite))

        # Set up delivery options.
        conversations = Conversations() if parse_data else []

        # Multi-threading to handle multiple requests at a time.
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:

            # Create all future requests for the rest of the offsets in the body's data range.
            future_requests = {
                executor.submit(self.conversations, body, offset,limit): offset for offset in range(0, count, 100)
            }

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

        return conversations

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
