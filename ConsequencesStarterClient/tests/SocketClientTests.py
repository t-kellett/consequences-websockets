import pytest

from SocketClient import SocketClient


def test_connect_to_server():
    # arrange
    socket_client = SocketClient("ws://51.141.52.52:1234")

    # act
    socket_client.send({"Hello": "Hello"})
    response = socket_client.receive()

    # assert
    assert response.message == "Welcome to Consequences, to get started send your name and room code."
