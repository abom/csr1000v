from csr1000v.auth import Auth
from csr1000v.interfaces import Interfaces
from csr1000v.http import Http
from csr1000v.ntp import Ntp

BASE_URL = "api/v1"


class Router:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port

        self.http = Http(self)
        self.auth = Auth(self)
        self.token = self.auth.get_token(username, password)

        self.interfaces = Interfaces(self)
        self.ntp = Ntp(self)

    @property
    def base_url(self):
        return f"https://{self.host}:{self.port}/{BASE_URL}"
