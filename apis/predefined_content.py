from lp_api_wrapper.util.wrapper_base import WrapperBase, APIMethod


class PredefinedContent(WrapperBase):
    """
    Python Wrapper for the LivePerson Predefined Categories API.

    Documentation:
    https://developers.liveperson.com/account-configuration-categories-introduction.html
    """

    def __init__(self, auth):

        super().__init__(auth=auth)

        # Establish Base URL
        domain = self.get_domain(account_id=auth.account_id, service_name='accountConfigReadWrite')
        self.base_url = 'https://{}/api/account/{}/configuration'.format(domain, auth.account_id)

    def get_predefined_content_items(self, include_deleted=None, sanitize_data=None, lang=None, select=None,
                                     group_by=None, skill_ids=None, ids=None, version=2.0):

        """
        Documentation:
        https://developers.liveperson.com/account-configuration-predefined-content-get-items.html

        :param include_deleted: bool
        :param sanitize_data: bool
        :param lang: str
        :param select: str
        :param group_by: str
        :param skill_ids: str
        :param ids: str
        :param version: float
        :return: Decoded JSON data
        """

        return self.process_request(
            method=APIMethod.GET,
            url='{}/engagement-window/canned-responses'.format(self.base_url),
            url_parameters={
                'include_deleted': include_deleted,
                'sanitize_data': sanitize_data,
                'lang': lang,
                'select': select,
                'group_by': group_by,
                'skill_ids': skill_ids,
                'ids': ids,
                'v': version
            }
        )
