import pytest

from SocketClient import SocketClient


@pytest.fixture()
def socket_client():
    client = SocketClient("ws://51.141.52.52:1234")
    client.send({"Hello": "Hello"})

    return client


def test_connect_to_server(socket_client):
    # act
    response = socket_client.receive()

    # assert
    assert response.message == "Welcome to Consequences, to get started send your name and room code."


def test_server_accepts_name_room_and_responds_with_instructions(socket_client):
    # arrange
    socket_client.receive()
    socket_client.send(
        {"Name": "Tom",
         "Room": "101"
         })

    # act
    response = socket_client.receive()

    # assert
    assert response.message == "Welcome to room '101'. Please answer your first question when all players have joined the room."


def test_server_returns_list_of_players_added_to_room(socket_client):
    # arrange
    socket_client.receive()
    socket_client.send(
        {"Name": "Tom",
         "Name": "Jerry",
         "Room": "101"
         })

    # act
    response = socket_client.receive()

    # assert
    assert response.players == ["Tom", "Jerry"]