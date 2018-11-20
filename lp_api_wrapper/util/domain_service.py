import requests


class DomainService:

    @staticmethod
    def get_domain(account_id, service_name):
        """
        Documentation:
        https://developers.liveperson.com/agent-domain-domain-api.html

        :param account_id: str <Required>
        :param service_name: str <Required>
        :return: str (Returns API base domain based on account id and service name)
        """

        # Generate request
        r = requests.get(
            url=f'http://api.liveperson.net/api/account/{account_id}/service/{service_name}/baseURI.json?version=1.0'
        )

        # Check request status
        if r.ok:
            try:
                return r.json()['baseURI']
            except KeyError:
                print(f'[Domain Error]: {r.json()}')
        else:
            try:
                print(f'[Domain Error]: {r.json()}')
            except ValueError:
                pass

            r.raise_for_status()
