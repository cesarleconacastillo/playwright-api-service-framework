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
@allure.story("Update Booking")
@allure.severity(
    allure.severity_level.CRITICAL
)
def test_partial_booking_update(
        auth_service,
        booking_service
):
    with allure.step(
            "Generate authentication token"
    ):
        # Get Token
        auth_request = AuthFactory.create()

        auth_response = auth_service.get_token(
            auth_request
        )
        token = auth_response.json()["token"]

    with allure.step(
            "Create booking"
    ):
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

    with allure.step(
            "Partially update booking"
    ):
        # Update booking (PATCH)

        booking = BookingFactory.partial_update()

        response = booking_service.partial_booking_update(
            booking_id,
            booking,
            token
        )

    with allure.step(
            "Validate update"
    ):

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