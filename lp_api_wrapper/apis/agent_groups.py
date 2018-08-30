from lp_api_wrapper.util.wrapper_base import WrapperBase, APIMethod


class AgentGroups(WrapperBase):
    """
    Python Wrapper for the LivePerson Users API.

    Documentation:
    https://developers.liveperson.com/administration-agent-groups-overview.html
    """

    def __init__(self, auth, access='r', company=None, source="LPApiWrapper"):

        super().__init__(auth=auth)

        # Establish base URL
        if access == 'r':
            service_name = 'accountConfigReadOnly'
        elif access == 'rw':
            service_name = 'accountConfigReadWrite'
        else:
            raise Exception('Access only accepts values \'r\' and \'rw\'')

        domain = self.get_domain(account_id=auth.account_id, service_name=service_name)
        self.version = '4.0'
        self.base_url = 'https://{}/api/account/{}/configuration/le-users/agentGroups'.format(domain, auth.account_id)
        self.company = company
        self.source = source


    def all_agent_groups(self, include_deleted=False):
        """
        Documentation:
        https://developers.liveperson.com/administration-get-all-agent-groups.html

        :param include_deleted: Boolean
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.GET,
            url='{}?v={}'.format(self.base_url, self.version),
            url_parameters={
                'include_deleted': include_deleted,
                'company': self.company,
                'source': self.source
            }
        )

    def get_group_by_id(self, group_id):
        """
        Documentation:
        https://developers.liveperson.com/administration-get-agent-groups-by-id.html

        :param group_id: Positive long number greater than zero
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.GET,
            url='{}/{}?v={}'.format(self.base_url, group_id, self.version)
        )
