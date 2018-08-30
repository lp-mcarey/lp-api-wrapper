from lp_api_wrapper.util.wrapper_base import WrapperBase, APIMethod


class AgentMetrics(WrapperBase):
    """
    Python Wrapper for the LivePerson Agent Metrics API.

    Documentation:
    https://developers.liveperson.com/data-messaging-agent-metrics-overview.html
    """

    def __init__(self, auth, company=None, source="LPApiWrapper"):

        super().__init__(auth=auth)

        # Establish base URL
        domain = self.get_domain(account_id=auth.account_id, service_name='msgHist')
        self.base_url = 'https://{}/messaging_history/api/account/{}/agent-view'.format(domain, auth.account_id)
        self.company = company
        self.source = source

    def agent_status(self, status=None, agent_ids=None, skill_ids=None, agent_group_ids=None, agent_presence=None,
                     connection_states=None):
        """
        Documentation:
        https://developers.liveperson.com/data-messaging-interactions-methods-agent-status.html

        :param status: List[str]
        :param agent_ids: List[str]
        :param skill_ids: List[str]
        :param agent_group_ids: List[str]
        :param agent_presence: Bool
        :param connection_states: List[str]
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.POST,
            url='{}/status'.format(self.base_url),
            body={
                'status': status,
                'agentIds': agent_ids,
                'skillIds': skill_ids,
                'agentGroupIds': agent_group_ids,
                'agentPresence': agent_presence,
                'connectionStates': connection_states
            },
            url_parameters = {
                 'company': self.company,
                 'source': self.source
            }
        )

    def summary(self, status=None, agent_ids=None, skill_ids=None, agent_group_ids=None):
        """
        Documentation:
        https://developers.liveperson.com/data-messaging-interactions-methods-summary.html

        :param status: List[str]
        :param agent_ids: List[str]
        :param skill_ids: List[str]
        :param agent_group_ids: List[str]
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.POST,
            url='{}/summary'.format(self.base_url),
            body={
                'status': status,
                'agentIds': agent_ids,
                'skillIds': skill_ids,
                'agentGroupIds': agent_group_ids
            }
        )
