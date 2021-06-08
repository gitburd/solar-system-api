from app.models.planet import Planet
import pytest
from app import create_app
from app import db


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_planets(app):
    first_planet = Planet(name="Earth",
                          description="Mostly Harmless", has_rings=False)
    second_planet = Planet(name="Galifray",
                           description="Very unharmless", has_rings=False)

    db.session.add_all([first_planet, second_planet])
    db.session.commit()
