from test_data.booking_factory import (
    BookingFactory
)
from validators.response_validator import ResponseValidator


def test_create_booking(
        booking_service
):

    booking = BookingFactory.create()

    response = booking_service.create_booking(
        booking
    )

    ResponseValidator.verify_status(
        response,
        200
    )

    body = response.json()

    assert body["booking"]["firstname"] == booking.firstname

    assert body["booking"]["lastname"] == booking.lastname