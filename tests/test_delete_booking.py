import allure

from test_data.auth_factory import AuthFactory
from test_data.booking_factory import BookingFactory
from validators.response_validator import ResponseValidator

@allure.title(
    "Verify user can delete a booking successfully"
)

@allure.feature("Booking")
@allure.story("Delete Booking")
@allure.severity(
    allure.severity_level.CRITICAL
)
def test_partial_booking_update(
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

    create_booking = booking_service.create_booking(
        booking
    )

    ResponseValidator.verify_status(
        create_booking,
        200
    )
    booking_id = create_booking.json()["bookingid"]

    # Delete booking (PATCH)

    response = booking_service.delete_booking(
        booking_id,
        token
    )

    ResponseValidator.verify_status(
        response,
        201
    )
    body = response.text()
    assert "Created" in body