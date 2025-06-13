from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]
    def test_cities_spain():
        response = client.get("/countries/Spain/cities")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0  # Spain should have at least one city
    
    def test_cities_nonexistent_country():
        response = client.get("/countries/Atlantis/cities")
        assert response.status_code == 404 or response.status_code == 400
    
    def test_monthly_average_spain():
        # Get a city and month from Spain for testing
        cities_response = client.get("/countries/Spain/cities")
        assert cities_response.status_code == 200
        cities = cities_response.json()
        assert len(cities) > 0
        city = cities[0]
    
        # Try January as a common month
        response = client.get(f"/countries/Spain/{city}/January")
        assert response.status_code == 200
        assert isinstance(response.json(), (int, float, dict, list))