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


def test_server_returns_question_when_room_created(socket_client):
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
    assert response.question == "Please enter an adjective, followed by a person's name"


def test_server_accepts_answer_and_returns_next_question(socket_client):
    # arrange
    socket_client.receive()
    socket_client.send(
        {"Name": "Tom",
         "Name": "Jerry",
         "Room": "102"  # different room as tests run too quickly
         })

    # act
    socket_client.receive()
    socket_client.send({
        "Answer": "Little Jerry"
    })
    response = socket_client.receive()

    # assert
    assert response.question == "Please enter another adjective, followed by a different person's name"
