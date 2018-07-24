import concurrent.futures
import math
import re
from lp_api_wrapper.parsers import Engagements
from lp_api_wrapper.util.wrapper_base import WrapperBase, APIMethod


class EngagementHistory(WrapperBase):
    """
    Python Wrapper for the LivePerson Engagement History API

    Documentation:
    https://developers.liveperson.com/data-engagement-history-methods.html
    """

    def __init__(self, auth):

        super().__init__(auth=auth)

        # Establish Base URL
        domain = self.get_domain(account_id=auth.account_id, service_name='engHistDomain')
        self.base_url = 'https://{}/interaction_history/api/account/{}'.format(domain, auth.account_id)

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

        return self.process_request(
            method=APIMethod.POST,
            url='{}/interactions/search'.format(self.base_url),
            url_parameters={
                'offset': offset,
                'limit': limit,
                'sort': sort
            },
            body=body
        )

    def all_engagements(self, body, max_workers=7, debug=0, parse_data=False):
        """
        Documentation:
        https://developers.liveperson.com/data_api-engagement-history-methods.html

        * Returns all offsets of data within start time range *

        :param body: dict <Required>
        :param max_workers: int (Max # of concurrent requests)
        :param debug: int (Status of API requests: 1=full, 2=summary, default=0)
        :param parse_data: bool (Returns a parsed Engagements data object.)
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

        # If there are no conversations in data range, return nothing.
        if count == 0:
            if debug == 1:
                print('[EHAPI Status]: There are 0 records!')
            return None
        else:
            if debug >= 1:
                print('[EHAPI Summary]: count=%s reqs=%s workers=%s leSite=%s' % (count, math.ceil(count/limit), max_workers, lesite))

        # Set up delivery options.
        engagements = Engagements() if parse_data else []

        # Multi-threading to handle multiple requests at a time.
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:

            # Create all future requests for the rest of the offsets in the body's data range.
            future_requests = {
                executor.submit(self.engagements, body, offset, limit): offset for offset in range(0, count, 100)
            }

            for future in concurrent.futures.as_completed(future_requests):

                if debug == 1:
                    print('[EHAPI Offset Status]: {} of {} records completed!'.format(future_requests[future], count))

                # Grab dict with 'interactionHistoryRecords' from the request.  Removing any '_metadata' info.
                records = future.result()['interactionHistoryRecords']

                # Store results
                if parse_data:
                    engagements.append_records(records=[record for record in records])
                else:
                    engagements.extend([record for record in records])

        return engagements

