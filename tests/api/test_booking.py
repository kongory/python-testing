import allure
import pytest
import requests


def create_booking(json_body):
    with allure.step('Create booking'):
        response = requests.post("https://restful-booker.herokuapp.com/booking", json=json_body)
    return response


@pytest.fixture
def authorize():
    login = "admin"
    password = "password123"
    with allure.step('Get token'):
        response = requests.post("https://restful-booker.herokuapp.com/auth",
                                 json={"username": login, "password": password})
    return response.json()["token"]


@allure.feature('Check booking API')
@allure.story('Receive all booking test')
def test_all_bookings():
    with allure.step('Get all bookings'):
        response = requests.get("https://restful-booker.herokuapp.com/booking")

    assert response.status_code == requests.codes.ok, f"Wrong status code: {response.status_code}"
    assert len(response.content) > 5, "Wrong count of bookings"


@allure.feature('Check booking API')
@allure.story('Create booking tests')
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
    response = create_booking(booking)
    id = response.json()["bookingid"]

    assert response.status_code == requests.codes.ok, f"Wrong status code: {response.status_code}"
    assert id > 0, "Booking isn't created"


@allure.feature('Check booking API')
@allure.story('Update created booking test')
def test_update_booking(authorize):
    token = authorize
    booking = {
        "firstname": "James",
        "lastname": "Bond",
        "totalprice": 3000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    id = create_booking(booking).json()["bookingid"]
    booking_edited = {
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
    with allure.step('Update booking'):
        response = requests.put(f"https://restful-booker.herokuapp.com/booking/{id}", json=booking_edited,
                                cookies=cookies)

    assert response.status_code == requests.codes.ok, f"Wrong status code: {response.status_code}"


@allure.feature('Check booking API')
@allure.story('Patch created booking test')
def test_patch_booking(authorize):
    token = authorize
    booking = {
        "firstname": "James",
        "lastname": "Bond",
        "totalprice": 1250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    id = create_booking(booking).json()["bookingid"]
    booking_edited = {
        "depositpaid": False,
        "additionalneeds": "Dinner"
    }

    cookies = {'token': token}
    with allure.step('Patch booking'):
        response = requests.patch(f"https://restful-booker.herokuapp.com/booking/{id}", json=booking_edited,
                                  cookies=cookies)

    assert response.status_code == requests.codes.ok, f"Wrong status code: {response.status_code}"


@allure.feature('Check booking API')
@allure.story('Get created booking by Id tests')
def test_get_by_id():
    booking = {
        "firstname": "James",
        "lastname": "Bond",
        "totalprice": 2100,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Launch"
    }
    id = create_booking(booking).json()["bookingid"]
    with allure.step('Get booking by Id'):
        response = requests.get(f"https://restful-booker.herokuapp.com/booking/{id}")

    assert response.json()["totalprice"] == 2100, f'Wrong price: {response.json()["totalprice"]}'
    assert response.json()["additionalneeds"] == "Launch", \
        f'Wrong additional needs: {response.json()["additionalneeds"]}'
    assert response.json()["depositpaid"] == False, f'Wrong depositpaid: {response.json()["depositpaid"]}'


@allure.feature('Check booking API')
@allure.story('Delete created booking by Id test')
def test_delete_booking(authorize):
    token = authorize
    booking = {
        "firstname": "James",
        "lastname": "Bond",
        "totalprice": 6000,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Launch"
    }
    id = create_booking(booking).json()["bookingid"]
    cookies = {'token': token}
    with allure.step('Delete booking'):
        response = requests.delete(f"https://restful-booker.herokuapp.com/booking/{id}", cookies=cookies)

    assert response.status_code == requests.codes.created
