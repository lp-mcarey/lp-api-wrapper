from requests_oauthlib import OAuth1


class OAuthLogin:
    """
    The OAuthLogin class will let you authenticate Python LiveEngage API Wrapper classes.
    """

    def __init__(self, account_id, app_key, app_secret, access_token=None, access_token_secret=None):

        self.account_id = account_id
        self.oauth = OAuth1(
            client_key=app_key,
            client_secret=app_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret
        )
