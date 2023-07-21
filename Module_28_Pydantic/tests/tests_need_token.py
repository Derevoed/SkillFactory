import pytest
import requests
from api.api import auth_token, create_booking
from serializers.orders import UpdateBookingRequest, UpdateBookingResponse, BookingResponseModel
from pydantic import ValidationError

# TESTS WITH TOKEN REQUIRED


@pytest.mark.required_token
@pytest.mark.parametrize('auth_token, create_booking, content_type, expected_status', [
    (auth_token(), create_booking(auth_token), 'application/json', 201),      # Valid token and data positive test
    ('asd324sda', create_booking(auth_token), 'application/json', 403),       # Invalid token and valid data negative test
    (auth_token(), '-1', 'application/json', 405),                            # Invalid bookingid and valid data negative test
    (auth_token(), create_booking(auth_token), 'text/plain', 415)])           # Invalid Content-Type and valid data negative test
def test_delete_booking(auth_token, create_booking, content_type, expected_status):

    url = f'https://restful-booker.herokuapp.com/booking/{create_booking}'
    headers = {
        'Content-Type': f'{content_type}',
        'Cookie': f'token={auth_token}'
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 201:
        assert response.status_code == expected_status, f'Delete booking request failed with status code {response.status_code}'
        assert response.text == 'Created', 'Delete booking response should contain "Created"'
    elif response.status_code == 403:
        assert response.status_code == expected_status, f'Delete booking request failed with status code {response.status_code}'
        assert response.text == 'Forbidden', 'Delete booking response should contain "Created"'
    elif response.status_code == 405:
        assert response.status_code == expected_status, f'Delete booking request failed with status code {response.status_code}'
        assert response.text == 'Method Not Allowed', 'Delete booking response should contain "Created"'
    elif response.status_code == 415:
        assert response.status_code == expected_status, f'Delete booking request failed with status code {response.status_code}'
        assert response.text == 'Unsupported Media Type', 'Delete booking response should contain "Created"'


@pytest.mark.required_token
@pytest.mark.parametrize('auth_token, create_booking, content_type, accept, request_body, expected_status', [
    (auth_token(), create_booking(auth_token), 'application/json', 'application/json',
     {"firstname": "James", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
      "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"}, "additionalneeds": "Breakfast"}, 200),   # Valid token and data positive test
    ('dfg6783jjd', create_booking(auth_token), 'application/json', 'application/json',
     {"firstname": "James", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
      "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"}, "additionalneeds": "Breakfast"}, 403),    # Invalid token and valid data negative test
    (auth_token(), '-1', 'application/json', 'application/json',
     {"firstname": "James", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
      "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"}, "additionalneeds": "Breakfast"}, 405),   # Invalid bookingid and valid data negative test
    (auth_token(), create_booking(auth_token), 'text/plain', 'text/plain',
     {"firstname": "James", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
      "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"}, "additionalneeds": "Breakfast"}, 415),    # Invalid Content-Type and Accept, valid data negative test
    (auth_token(), create_booking(auth_token), None, None,
     {"firstname": "James", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
      "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"}, "additionalneeds": "Breakfast"}, 400)    # No Content-Type and Accept, valid data negative test
])
def test_update_booking(auth_token, create_booking, content_type, accept, request_body, expected_status):
    url = f'https://restful-booker.herokuapp.com/booking/{create_booking}'
    headers = {
        'Content-Type': f'{content_type}',
        'Accept': f'{content_type}',
        'Cookie': f'token={auth_token}'
    }

    try:
        request_data = UpdateBookingRequest(**request_body)
    except ValidationError as e:
        pytest.fail(f"Failed to validate request data: {e}")

    response = requests.put(url, headers=headers, json=request_data.model_dump())

    assert response.status_code == expected_status, f"Request failed with status code {response.status_code}"

    if expected_status == 200:
        try:
            response_data = response.json()
            updating_response = UpdateBookingResponse(**response_data)
        except (ValidationError, TypeError) as e:
            pytest.fail(f"Failed to validate booking update response data: {e}")

        get_headers = {
            'Accept': 'application/json'
        }
        get_updated_booking = requests.get(url, headers=get_headers)
        get_data = get_updated_booking.json()
        get_booking = BookingResponseModel(**get_data) and UpdateBookingResponse(**response_data)

        assert get_booking.firstname == request_data.firstname, "Invalid firstname in the response"
        assert get_booking.lastname == request_data.lastname, "Invalid lastname in the response"
        assert get_booking.totalprice == request_data.totalprice, "Invalid totalprice in the response"
        assert get_booking.depositpaid == request_data.depositpaid, "Invalid depositpaid in the response"
        assert get_booking.bookingdates.model_dump() == request_data.bookingdates.model_dump(), "Invalid bookingdates in the response"
        assert get_booking.additionalneeds == request_data.additionalneeds, "Invalid additionalneeds in the response"
