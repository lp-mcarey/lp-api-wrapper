import concurrent.futures
import math
import re
import time
from lp_api_wrapper.parsers import Engagements
from lp_api_wrapper.util.wrapper_base import WrapperBase, APIMethod


class EngagementHistory(WrapperBase):
    """
    Python Wrapper for the LivePerson Engagement History API

    Documentation:
    https://developers.liveperson.com/data-engagement-history-methods.html
    """

    def __init__(self, auth, company=None, source="LPApiWrapper"):

        super().__init__(auth=auth)

        # Establish Base URL
        domain = self.get_domain(account_id=auth.account_id, service_name='engHistDomain')
        self.base_url = 'https://{}/interaction_history/api/account/{}'.format(domain, auth.account_id)
        self.company = company
        self.source = source

    def engagements(self, body, offset=0, limit=100, sort=None):
        """
        Documentation:
        https://developers.liveperson.com/data_api-engagement-history-methods.html

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
        for trial in range(1, num_retries):
            if (error):
                try:
                    api_return = self.process_request(
                        method=APIMethod.POST,
                        url='{}/interactions/search'.format(self.base_url),
                        url_parameters={
                            'offset': offset,
                            'limit': limit,
                            'sort': sort,
                            'company': self.company,
                            'source': self.source
                        },
                        body=body
                    )
                    error = False
                    return api_return
                except Exception:
                    time.sleep(trial * wait_time)

    def all_engagements(self, body, max_workers=7, debug=0, parse_data=False, offset=0, max_limit=None):
        """
        Documentation:
        https://developers.liveperson.com/data_api-engagement-history-methods.html

        * Returns all offsets of data within start time range *

        :param body: dict <Required>
        :param max_workers: int (Max # of concurrent requests)
        :param debug: int (Status of API requests: 1=full, 2=summary, default=0)
        :param parse_data: bool (Returns a parsed Engagements data object.)
        :param offset: Start offset
        :param max_limit: Max conversations to retrieve. Default -1, is all conversations based on the body
        :return List of interaction history records as decoded JSON data
        """

        # Grab first offset of data.
        initial_data = self.engagements(body=body, offset=0)

        # Number of conversations in date range that was selected in the body start parameters.
        count = initial_data['_metadata']['count']

        # Retrieve site ID from URL
        lesite = re.search('account/(.*)', self.base_url)
        lesite = lesite.group(1)

        # Max number of retrivals per call
        limit = 100
        offset_start = offset
        # Total number of conversation to actually retrieve
        if (max_limit is None):
            total_conversation = count - offset
            last_conversation = count
        else:
            if (count > max_limit + offset):
                total_conversation = max_limit
                last_conversation = max_limit + offset
            else:
                total_conversation = count - offset
                last_conversation = count

        # If there are no conversations in data range, return nothing.
        if count == 0:
            if debug == 1:
                print('[EHAPI Status]: There are 0 records!')
            return None
        else:
            if debug >= 1:
                print('[EHAPI Summary]: count=%s reqs=%s workers=%s leSite=%s' % (total_conversation, math.ceil(total_conversation/limit), max_workers, lesite))

        # Set up delivery options.
        engagements = Engagements() if parse_data else []

        # Multi-threading to handle multiple requests at a time.
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:

            # Create all future requests for the rest of the offsets in the body's data range.
            future_requests = {}
            last_call = False
            while (not last_call):
                if (offset_start + limit >= last_conversation):
                    limit = last_conversation - offset_start
                    future_requests[executor.submit(self.engagements, body, offset_start, limit)] = offset_start
                    last_call = True
                else:
                    future_requests[executor.submit(self.engagements, body, offset_start, limit)] = offset_start
                    offset_start = offset_start + limit

            for future in concurrent.futures.as_completed(future_requests):

                if debug == 1:
                    print('[EHAPI Offset Status]: {} of {} records completed!'.format(future_requests[future] - offset, total_conversation ))

                # Grab dict with 'interactionHistoryRecords' from the request.  Removing any '_metadata' info.
                records = future.result()['interactionHistoryRecords']

                # Store results
                if parse_data:
                    engagements.append_records(records=[record for record in records])
                else:
                    engagements.extend([record for record in records])

        return engagements

    def all_engagements_by_chunks(self, body, max_workers=7, debug=0, parse_data=False):
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
        initial_data = self.engagements(body=body, offset=0)

        # Number of conversations in date range that was selected in the body start parameters.
        count = initial_data['_metadata']['count']

        # Retrieve site ID from URL
        lesite = re.search('account/(.*)', self.base_url)
        lesite = lesite.group(1)

        # Max number of retrivals per call
        limit_per_call = 100

        # If there are no conversations in data range, return nothing.
        if count == 0:
            if debug == 1:
                print('[EHAPI Status]: There are 0 records!')
            return None
        else:
            if debug >= 1:
                print('[EHAPI Summary]: count=%s reqs=%s workers=%s leSite=%s' % (count, math.ceil(count/limit_per_call), max_workers, lesite))
            chunk_size = 500 # MUST be greater than the limit_per_call
            chunk_offset = 0
            offset = 0
            chunks = math.ceil(count/chunk_size)

        # E.g Count =468, chunk_size =150 then chunks 4
        # Will iterate 4 times
        for iterat in range(1, chunks + 1):
            engagements = Engagements() if parse_data else []
            future_requests = {}
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:

                # First iteration: chunk_offset =0 , chunk_offset + chunk_size = 150 , limit_per_call=100,  list_offset = [0,100]
                # Second iteration:  chunk_offset =150 , chunk_offset + chunk_size = 300 , limit_per_call=100,  list_offset = [150,250]
                # Fourth iteration: list_offset = [450,600]
                list_offset = range(chunk_offset, chunk_offset + chunk_size, limit_per_call)
                for elem in list_offset:
                    if(elem < count): # If the element is greater than the total count, we dont need to make a call starting with that offset. Fourth iteration 600>468
                        if (elem + limit_per_call > chunk_offset + chunk_size): # For second iteration, second element: 250 + 100 > 150 + 150; For fourth iteration, second element: won't pass previous if
                            limit_per_call = chunk_size - limit_per_call # 150 - 100 = 50
                        future_requests[executor.submit(self.engagements, body, offset, limit_per_call)] = offset
                        offset = offset + limit_per_call


                for future in concurrent.futures.as_completed(future_requests):

                    if debug == 1:
                        print('[EHAPI Offset Status]: {} of {} records completed!'.format(future_requests[future], count))

                    # Grab dict with 'conversationHistoryRecords' from the request.  Removing any '_metadata' info.
                    records = future.result()['interactionHistoryRecords']

                    # Store results.
                    if parse_data:
                        engagements.append_records(records=[record for record in records])
                    else:
                        engagements.extend([record for record in records])

                limit_per_call = 100
                chunk_offset = chunk_offset + chunk_size
            yield engagements

