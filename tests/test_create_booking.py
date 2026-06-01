import allure

from test_data.booking_factory import (
    BookingFactory
)
from validators.response_validator import ResponseValidator

@allure.title(
    "Verify user can create a booking successfully"
)

@allure.feature("Booking")
@allure.story("Create Booking")
@allure.severity(
    allure.severity_level.CRITICAL
)
def test_create_booking(
        booking_service
):
    with allure.step(
            "Generate booking test data"
    ):

        booking = BookingFactory.create()

    with allure.step(
            "Create booking through API"
    ):

        response = booking_service.create_booking(
        booking
        )

    with allure.step(
            "Validate status code"
    ):

        ResponseValidator.verify_status(
            response,
            200
        )

    with allure.step(
            "Validate booking details"
    ):
        body = response.json()

        assert body["booking"]["firstname"] == booking.firstname
        assert body["booking"]["lastname"] == booking.lastname