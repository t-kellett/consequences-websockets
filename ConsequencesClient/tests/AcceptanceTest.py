def test_full_run_of_consequences(socket_client):
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
    socket_client.receive()
    socket_client.send({
        "Answer": "Big Tom"
    })
    socket_client.receive()
    socket_client.send({
        "Answer": "the mousetrap"
    })
    socket_client.receive()
    socket_client.send({
        "Answer": "to fight"
    })
    socket_client.receive()
    socket_client.send({
        "Answer": "Tom swung his comedy hammer"
    })
    socket_client.receive()
    socket_client.send({
        "Answer": "Jerry ran around in circles"
    })
    socket_client.receive()
    socket_client.send({
        "Answer": "Tom hit the mousetrap and caught his foot in it"
    })
    response = socket_client.receive()
    second_game = socket_client.receive()

    # assert
    assert response.results == ['Little Jerry met Big Tom at the mousetrap to to fight. Jerry Tom swung his comedy hammer, whilst Tom Jerry ran around in circles. The consequence of their actions was Tom hit the mousetrap and caught his foot in it.']