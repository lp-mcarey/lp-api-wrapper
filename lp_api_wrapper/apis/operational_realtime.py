from lp_api_wrapper.util.wrapper_base import WrapperBase, APIMethod


class OperationalRealtime(WrapperBase):
    """
    Python Wrapper for the LivePerson Operational Realtime API.

    Documentation:
    https://developers.liveperson.com/data-operational-realtime-overview.html
    """

    def __init__(self, auth, company=None, source="LPApiWrapper"):

        super().__init__(auth=auth)

        # Establish Base URL
        domain = self.get_domain(account_id=auth.account_id, service_name='leDataReporting')
        self.base_url = 'https://{}/operations/api/account/{}'.format(domain, auth.account_id)
        self.company = company
        self.source = source

    def queue_health(self, time_frame, skill_ids=None, interval=None, version=1):
        """
        Documentation:
        https://developers.liveperson.com/data-operational-realtime-queue-health.html

        Retrieves queue-related metrics at the account or skill level.

        :param time_frame: int <Required>
        :param skill_ids: str
        :param interval: int
        :param version: int
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.GET,
            url='{}/queuehealth'.format(self.base_url),
            url_parameters={
                'timeframe': time_frame,
                'v': version,
                'skillIds': skill_ids,
                'interval': interval,
                'company': self.company,
                'source': self.source
            }
        )

    def engagement_activity(self, time_frame, skill_ids=None, agent_ids=None, interval=None, version=1):
        """
        Documentation:
        https://developers.liveperson.com/data-operational-realtime-engagement-activity.html


        :param time_frame: int <Required>
        :param skill_ids: str
        :param agent_ids: str
        :param interval: int
        :param version: int
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.GET,
            url='{}/engactivity'.format(self.base_url),
            url_parameters={
                'timeframe': time_frame,
                'v': version,
                'agentIds': agent_ids,
                'skillIds': skill_ids,
                'interval': interval
            }
        )

    def agent_activity(self, time_frame, agent_ids, interval=None, version=1):
        """
        Documentation:
        https://developers.liveperson.com/data-operational-realtime-agent-activity.html

        :param time_frame: int <Required>
        :param agent_ids: str <Required>
        :param interval: int
        :param version: int
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.POST,
            url='{}/agentactivity'.format(self.base_url),
            body={
                'timeframe': time_frame,
                'agentIds': agent_ids,
                'v': version,
                'interval': interval
            }
        )

    def current_queue_state(self, skill_ids=None, version=1):
        """
        Documentation:
        https://developers.liveperson.com/data-operational-realtime-current-queue-state.html

        :param skill_ids: str
        :param version: int
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.GET,
            url='{}/queuestate'.format(self.base_url),
            url_parameters={
                'v': version,
                'skillIds': skill_ids
            }
        )

    def sla_histogram(self, time_frame, skill_ids=None, group_ids=None, histogram=None, version=1):
        """
        Documentation:
        https://developers.liveperson.com/data-operational-realtime-sla-histogram.html

        :param time_frame: int <Required>
        :param skill_ids: str
        :param group_ids: str
        :param histogram: str
        :param version: int
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.GET,
            url='{}/sla'.format(self.base_url),
            url_parameters={
                'timeframe': time_frame,
                'v': version,
                'skillIds': skill_ids,
                'groupIds': group_ids,
                'histogram': histogram
            }
        )
