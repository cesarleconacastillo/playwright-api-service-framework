import allure

from test_data.booking_factory import BookingFactory
from validators.response_validator import ResponseValidator

@allure.title(
    "Verify user can get a booking successfully"
)

@allure.feature("Booking")
@allure.story("Get Booking by ID")
@allure.severity(
    allure.severity_level.CRITICAL
)
def test_get_booking_by_id(
        booking_service
):
    booking = BookingFactory.create()

    response = booking_service.create_booking(
        booking
    )

    response_body = response.json()
    booking_id = response_body['bookingid']

    response_get = booking_service.get_booking(
        booking_id
    )

    ResponseValidator.verify_status(
        response,
        200
    )