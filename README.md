# csr1000v

An example for a python client for csr1000v router, only simple interface and ntp operations are implemented for now.

## Usage example

```python
from csr1000v import Router

host, port = "172.18.0.3", 55443
router = Router(host, port, "abdo", "1234")
print(router.token)
print(router.interfaces.list_all())
```
