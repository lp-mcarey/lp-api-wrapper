from lp_api_wrapper.util.wrapper_base import WrapperBase, APIMethod


class MessagingOperations(WrapperBase):
    """
    Python Wrapper for the LivePerson Messaging Operations API.

    Documentation:
    https://developers.liveperson.com/data-messaging-operations-overview.html
    """

    def __init__(self, auth, company=None, source="LPApiWrapper"):

        super().__init__(auth=auth)

        # Establish Base URL
        domain = self.get_domain(account_id=auth.account_id, service_name='leDataReporting')
        self.base_url = 'https://{}/operations/api/account/{}'.format(domain, auth.account_id)

        ewt_domain = self.get_domain(account_id=auth.account_id, service_name='msgEwtAPI')
        self.ewt_base_url = 'https://{}/lp-messaging-ewt-app/api/account/{}'.format(ewt_domain, auth.account_id)
        self.company = company
        self.source = source

    def messaging_conversation(self, time_frame, skill_ids=None, agent_ids=None, interval=None, version=1):
        """
        Documentation:
        https://developers.liveperson.com/data-messaging-operations-messaging-conversation.html

        :param time_frame: int <Required>
        :param skill_ids: str
        :param agent_ids: str
        :param interval: int
        :param version: int
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.POST,
            url='{}/msgconversation'.format(self.base_url),
            body={
                'timeframe': time_frame,
                'v': version,
                'skillIds': skill_ids,
                'agentIds': agent_ids,
                'interval': interval
            },
            url_parameters={
                'company': self.company,
                'source': self.source
            }

        )

    def messaging_current_queue_health(self,  skill_ids=None, version=1):
        """
        Documentation:
        https://developers.liveperson.com/data-messaging-operations-messaging-current-queue-health.html

        :param skill_ids: str
        :param version: int
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.GET,
            url='{}/msgqueuehealth/current'.format(self.base_url),
            url_parameters={
                'v': version,
                'skillIds': skill_ids
            }
        )

    def messaging_queue_health(self, time_frame, skill_ids=None, interval=None, version=1):
        """
        Documentation:
        https://developers.liveperson.com/data-messaging-operations-messaging-queue-health.html

        :param time_frame: int <Required>
        :param skill_ids: str
        :param interval: int
        :param version: int
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.GET,
            url='{}/msgqueuehealth'.format(self.base_url),
            url_parameters={
                'timeframe': time_frame,
                'v': version,
                'skillIds': skill_ids,
                'interval': interval
            }
        )

    def messaging_csat_distribution(self, time_frame, skill_ids=None, agent_ids=None, version=1):
        """
        Documentation:
        https://developers.liveperson.com/data-messaging-operations-messaging-csat-distribution.html

        :param time_frame: int <Required>
        :param skill_ids: str
        :param agent_ids: str
        :param version: int
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.GET,
            url='{}/msgcsatdistribution'.format(self.base_url),
            url_parameters={
                'timeframe': time_frame,
                'v': version,
                'skillIds': skill_ids,
                'agentIds': agent_ids
            }
        )
    
    def messaging_estimated_wait_time(self, skill_ids=None, version=1):
        """
        Documentation:
        https://developers.liveperson.com/data-messaging-operations-messaging-estimated-wait-time.html
        
        :param skill_ids: str
        :param version: int
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.GET,
            url='{}/ewt'.format(self.ewt_base_url),
            url_parameters={
                'skills': skill_ids,
                'v': version
            }
        )
