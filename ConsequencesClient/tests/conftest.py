import pytest

from SocketClient import SocketClient


@pytest.fixture()
def socket_client():
    client = SocketClient("ws://51.141.52.52:1234")
    client.send({"Hello": "Hello"})

    return client
