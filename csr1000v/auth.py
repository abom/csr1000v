from urllib.parse import urljoin


class Auth:
    def __init__(self, router):
        self.router = router

    @property
    def base_url(self):
        return self.router.base_url + "/auth/token-services"

    def get_token(self, username, password):
        data = self.router.http.json_call(self.base_url, "post", basic_auth=(username, password))
        return data["token-id"]

    def invalidate(self, token):
        url = urljoin(self.base_url, token)
        self.router.http.call(url, "delete")
