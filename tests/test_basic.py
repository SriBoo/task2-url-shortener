import pytest
from app.main import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['service'] == 'URL Shortener API'

def test_api_health(client):
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'
    assert data['message'] == 'URL Shortener API is running'

def test_shorten_and_redirect(client):
    url_data = {"url": "https://example.com"}
    response = client.post('/shorten', data=json.dumps(url_data), content_type='application/json')
    assert response.status_code == 201
    data = response.get_json()
    assert "short_url" in data
    assert "original_url" in data
    assert data["original_url"] == url_data["url"]

    # Extract short code
    short_url = data["short_url"]
    short_code = short_url.rsplit('/', 1)[-1]

    # Test redirection
    redirect_response = client.get(f'/{short_code}', follow_redirects=False)
    assert redirect_response.status_code == 302
    assert redirect_response.headers["Location"] == url_data["url"]
