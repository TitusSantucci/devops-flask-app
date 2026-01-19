from app import app

<<<<<<< HEAD
def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
=======
def test_home_status_code():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
>>>>>>> 5770a1f (Add requirements and basic test)
