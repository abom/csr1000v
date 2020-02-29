class Ntp:
    def __init__(self, router):
        self.router = router

    @property
    def base_url(self):
        return self.router.base_url + "/global/ntp/servers"

    def list_all(self):
        resp = self.router.http.auth_call(self.base_url, "get")
        return resp.json()["items"]

