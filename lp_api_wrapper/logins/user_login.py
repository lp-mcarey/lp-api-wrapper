import requests
from datetime import datetime
from lp_api_wrapper.util.domain_service import DomainService


class UserLogin(DomainService):
    """
    The UserLogin class allows other Python LiveEngage API Wrapper classes to login via the Login Service API.

    Documentation:
    https://developers.liveperson.com/login-getting-started.html
    """

    def __init__(self, account_id, username, password):

        self.account_id = account_id
        self.username = username
        self.password = password
        self.bearer = None
        self.timestamp = None

        domain = self.get_domain(account_id=account_id, service_name='agentVep')
        self.base_url = 'https://{}/api/account/{}'.format(domain, account_id)

        # Generate bearer token upon initialization.
        self.login()

    def login(self):
        """
        Documentation:
        https://developers.liveperson.com/agent-user-login.html

        Generates Bearer and CSRF tokens.
        """

        # Generate request
        r = requests.post(
            url='{}/login'.format(self.base_url),
            params={
                'v': '1.3'
            },
            json={
                'username': self.username,
                'password': self.password
            },
            headers={
                'content-type': 'application/json',
                'accept': 'application/json'
            }
        )

        # Check request status
        if r.ok:
            try:
                self.timestamp = datetime.now()
                self.bearer = r.json()['bearer']
            except KeyError:
                print('Oh noes! ~ Could not get bearer token! :( \n{}'.format(r.json()))
        else:
            try:
                print('Whoops! ~ Something went wrong! :( \n{}'.format(r.json()))
            except ValueError:
                pass

            r.raise_for_status()
