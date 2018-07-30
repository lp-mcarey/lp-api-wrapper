from lp_api_wrapper.util.wrapper_base import WrapperBase, APIMethod


class AdminUsers(WrapperBase):
    """
    Python Wrapper for the LivePerson Users API.

    Documentation:
    https://developers.liveperson.com/administration-users-overview.html
    """

    def __init__(self, auth, access='r'):

        super().__init__(auth=auth)

        # Establish base URL
        if access == 'r':
            service_name = 'accountConfigReadOnly'
        elif access == 'rw':
            service_name = 'accountConfigReadWrite'
        else:
            print('Access only accepts values \'r\' and \'rw\'')

        domain = self.get_domain(account_id=auth.account_id, service_name=service_name)
        self.version = '4.0'
        self.base_url = 'https://{}/api/account/{}/configuration/le-users/users'.format(domain, auth.account_id)


    def all_users(self, select='id,pid,deleted,loginName', include_deleted=False):
        """
        Documentation:
        https://developers.liveperson.com/administration-get-all-users.html

        :param select: YOGA 'gdata' dialect.
        :param include_deleted: Boolean
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.GET,
            url='{}?v={}'.format(self.base_url, self.version),
            url_parameters={
                'select': select,
                'include_deleted': include_deleted
            }
        )

    def get_user_by_id(self, user_id, select='id,pid,deleted,userTypeId,isApiUser,email,loginName,nickname,fullName,'
                                             'employeeId,isEnabled,maxChats,maxAsyncChats,skillIds,'
                                             'memberOf(agentGroupId,assignmentDate),'
                                             'managerOf(agentGroupId,assignmentDate),profileIds,lobIds'):
        """
        Documentation:
        https://developers.liveperson.com/administration-get-user-by-id.html

        :param select: YOGA 'gdata' dialect.
        :param user_id: Positive long number greater than zero
        :return Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.GET,
            url='{}/{}?v={}'.format(self.base_url, user_id, self.version),
            url_parameters={
                'select': select
            }
        )
