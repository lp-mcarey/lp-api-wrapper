from collections import namedtuple
from datetime import datetime
import requests
from enum import Enum
from lp_api_wrapper.util.domain_service import DomainService
from lp_api_wrapper.logins.user_login import UserLogin
from lp_api_wrapper.logins.oauth_login import OAuthLogin
from lp_api_wrapper.util.wrapper_exception import WrapperException

LoginToken = namedtuple('LoginToken', ['bearer', 'oauth'])


class APIMethod(Enum):
    GET = 1
    POST = 2


class WrapperBase(DomainService):

    def __init__(self, auth):

        if type(auth) not in [UserLogin, OAuthLogin]:
            raise TypeError('Accepts UserLogin or OAuthLogin for authentication. Import from lp_api_wrapper.')

        self.auth = auth

    def _create_login_token(self):
        """
        :return: A namedtuple which contains either a bearer token or OAuth1 object.
        """

        bearer = None
        oauth = None

        # Check Auth Type
        if type(self.auth) == UserLogin:

            time_difference = datetime.now() - self.auth.timestamp

            # If the time difference is greater than 3 minutes (180 seconds), then get a new bearer token.
            if time_difference.seconds > 180:
                self.auth.login()
                print('[LP API WRAPPER]: New bearer token created!')

            bearer = 'Bearer {}'.format(self.auth.bearer)

        elif type(self.auth) == OAuthLogin:

            oauth = self.auth.oauth

        return LoginToken(bearer=bearer, oauth=oauth)

    def process_request(self, method, url, url_parameters=None, body=None, headers=None):
        """
        A helper function to process the results from a request.

        :param method: Use APIMethod class to choose between GET or POST method.
        :param url: str
        :param url_parameters: dict
        :param body: dict
        :param headers: dict
        :return:
        """

        # For Bearer Token or OAuth1 authorization.
        login_token = self._create_login_token()

        request_args = {
            'url': url,
            'params': url_parameters,
            'json': body,
            'headers': {
                'content-type': 'application/json',
                'authorization': login_token.bearer
            },
            'auth': login_token.oauth
        }

        if headers:
            request_args['headers'].update(headers)

        # Choose between GET or POST method.
        if method == APIMethod.GET:
            r = requests.get(**request_args)
        elif method == APIMethod.POST:
            r = requests.post(**request_args)
        else:
            raise ValueError('Must be APIMethod.GET or APIMethod.POST')

        # Check request status
        if r.ok:
            return r.json()
        else:
            print('Wrapper Exception: {}'.format(r.json()))
            raise WrapperException
