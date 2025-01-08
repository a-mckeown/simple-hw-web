import pytest
from simple-web-app import app  # Import simple Flask app

@pytest.fixture
def client():
    """Flask test client fixture."""
    with app.test_client() as client:
        yield client

def test_get_index(client):
    """Test the GET request to the index route."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Calculate" in response.data  # Check for specific text in the HTML response