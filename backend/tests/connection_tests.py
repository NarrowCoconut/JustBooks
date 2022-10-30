import requests

# test api route /profile
def test_profile():
    response = requests.get('http://localhost:5000/profile')