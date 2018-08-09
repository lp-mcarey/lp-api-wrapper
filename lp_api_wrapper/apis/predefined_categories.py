from lp_api_wrapper.util.wrapper_base import WrapperBase, APIMethod


class PredefinedCategories(WrapperBase):
    """
    Python Wrapper for the LivePerson Predefined Categories API.

    Documentation:
    https://developers.liveperson.com/account-configuration-categories-introduction.html
    """

    def __init__(self, auth, company=None, source="LPApiWrapper"):

        super().__init__(auth=auth)

        # Establish Base URL
        domain = self.get_domain(account_id=auth.account_id, service_name='accountConfigReadWrite')
        self.base_url = 'https://{}/api/account/{}'.format(domain, auth.account_id)
        self.company = company
        self.source = source

    def categories_list(self, select=None, include_deleted=None, version=2.0):
        """
        Documentation:
        https://developers.liveperson.com/account-configuration-predefined-list.html

        :param select: str
        :param include_deleted: bool
        :param version: float
        :return: Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.GET,
            url='{}/configuration/le-categories/categories'.format(self.base_url),
            url_parameters={
                'v': version,
                'select': select,
                'include_deleted': include_deleted,
                'company': self.company,
                'source': self.source
            }
        )
