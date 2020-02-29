class Interfaces:
    def __init__(self, router):
        self.router = router

    @property
    def base_url(self):
        return self.router.base_url + "/interfaces"

    def list_all(self):
        resp = self.router.http.auth_call(self.base_url, "get")
        return resp.json()["items"]

    def get_state(self, if_name):
        url = self.base_url + f"/{if_name}/state"
        resp = self.router.http.auth_call(url, "get")
        return resp.json()["enabled"]

    def set_state(self, if_name, state):
        url = self.base_url + f"/{if_name}/state"
        data = {"if-name": if_name, "enabled": state}
        self.router.http.auth_call(url, "put", data=data)
