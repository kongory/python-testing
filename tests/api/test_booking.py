import pytest
import requests

id = 0
token = ''


@pytest.fixture
def authorize():
    login = "admin"
    password = "password123"
    response = requests.post("https://restful-booker.herokuapp.com/auth",
                             json={"username": login, "password": password})
    global token
    token = response.json()["token"]


def test_all_bookings():
    response = requests.get("https://restful-booker.herokuapp.com/booking")

    assert response.status_code == 200
    assert len(response.content) > 5


def test_create_booking():
    booking = {
        "firstname": "James",
        "lastname": "Bond",
        "totalprice": 1200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post("https://restful-booker.herokuapp.com/booking", json=booking)
    global id
    id = response.json()["bookingid"]

    assert response.status_code == 200


def test_update_booking(authorize):
    booking = {
        "firstname": "James",
        "lastname": "Bond",
        "totalprice": 2100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    cookies = {'token': token}
    response = requests.put(f"https://restful-booker.herokuapp.com/booking/{id}", json=booking, cookies=cookies)

    assert response.status_code == 200


def test_patch_booking(authorize):
    booking = {
        "depositpaid": False,
        "additionalneeds": "Dinner"
    }

    cookies = {'token': token}
    response = requests.patch(f"https://restful-booker.herokuapp.com/booking/{id}", json=booking, cookies=cookies)

    assert response.status_code == 200


def test_get_by_id():
    response = requests.get(f"https://restful-booker.herokuapp.com/booking/{id}")

    assert response.json()["totalprice"] == 2100
    assert response.json()["additionalneeds"] == "Dinner"
    assert response.json()["depositpaid"] == False


def test_delete_booking(authorize):
    cookies = {'token': token}
    response = requests.delete(f"https://restful-booker.herokuapp.com/booking/{id}", cookies=cookies)

    assert response.status_code == 201
