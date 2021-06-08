from app.models.planet import Planet


def test_get_planets_with_no_records(client):
    response = client.get("/planets/")

    assert response.status_code == 200
    assert response.get_json() == []


def test_get_planets_with_two_records(client, two_saved_planets):
    response = client.get("/planets/")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body == [
        {
            "id": 1,
            "name": "Earth",
            "description": "Mostly Harmless",
            "has_rings": False
        },
        {
            "id": 2,
            "name": "Galifray",
            "description": "Very unharmless",
            "has_rings": False
        }
    ]


def test_get_planets_by_valid_id(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Earth",
        "description": "Mostly Harmless",
        "has_rings": False
    }]


def test_get_planets_by_invalid_id(client):
    response = client.get("/planets/4")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == None


def test_post_planet(client):
    response = client.post("/planets/", json={
        "name": "Earth",
        "description": "Mostly Harmless",
        "has_rings": False
    })

    assert response.status_code == 201
