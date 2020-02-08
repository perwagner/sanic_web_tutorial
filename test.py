from main import app


def test__index__get_request__returns_200():
    request, response = app.test_client.get('/')
    assert response.status == 200