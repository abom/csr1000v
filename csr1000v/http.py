import requests

HEADERS = {"Accept": "application/json", "Content-Type": "application/json"}


class Http:
    def __init__(self, router):
        self.router = router

    def call(self, url, method, data=None, headers=None, basic_auth=None):
        if headers:
            headers.update(HEADERS)
        else:
            headers = HEADERS

        return requests.request(method, url, auth=basic_auth, headers=headers, json=data, verify=False)

    def json_call(self, url, method, data=None, basic_auth=None):
        resp = self.call(url, method, data, basic_auth=basic_auth)
        return resp.json()

    def auth_call(self, url, method, data=None):
        token = self.router.token
        return self.call(url, method, data, headers={"x-auth-token": token})
