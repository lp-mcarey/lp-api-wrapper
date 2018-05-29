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
            url='http://api.liveperson.net/api/account/{}/service/{}/baseURI.json?version=1.0'.format(
                account_id,
                service_name
            )
        )

        # Check request status
        if r.ok:
            try:
                return r.json()['baseURI']
            except KeyError:
                print('Whoops! ~ Could not get domain! :( \n{}'.format(r.json()))
        else:
            try:
                print('Whoops! ~ Something went wrong! :( \n{}'.format(r.json()))
            except ValueError:
                pass

            r.raise_for_status()
