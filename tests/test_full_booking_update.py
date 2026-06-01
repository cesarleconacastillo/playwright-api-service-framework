import allure

from test_data.booking_factory import (
    BookingFactory,
)
from test_data.auth_factory import(
    AuthFactory
)
from validators.response_validator import ResponseValidator

@allure.title(
    "Verify user can update a booking successfully"
)

@allure.feature("Booking")
@allure.story("Full Update Booking")
@allure.severity(
    allure.severity_level.CRITICAL
)
def test_full_booking_update(
        auth_service,
        booking_service
):
    # Get Token
    auth_request = AuthFactory.create()

    auth_response = auth_service.get_token(
        auth_request
    )
    token = auth_response.json()["token"]

    # Create booking (POST)
    booking = BookingFactory.create()

    create_booking_response = booking_service.create_booking(
        booking
    )

    ResponseValidator.verify_status(
        create_booking_response,
        200
    )

    booking_id = create_booking_response.json()["bookingid"]

    # Update booking (PATCH)

    booking = BookingFactory.create()

    response = booking_service.full_booking_update(
        booking_id,
        booking,
        token
    )

    ResponseValidator.verify_status(
        response,
        200
    )

    body = response.json()

    assert body["firstname"] == booking.firstname

    assert body["lastname"] == booking.lastname

    response = booking_service.delete_booking(
        booking_id,
        token
    )

    ResponseValidator.verify_status(
        response,
        201
    )