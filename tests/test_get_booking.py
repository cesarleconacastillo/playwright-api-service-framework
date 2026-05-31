from test_data.booking_factory import BookingFactory
from validators.response_validator import ResponseValidator


def test_get_booking(
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

    response_body_get = response_get.json()

    print(response_body_get)