from app.models.planet import Planet


def test_get_planets_with_no_records(client):
    response = client.get("/planets/")

    assert response.status_code == 200
    assert response.get_json() == []
