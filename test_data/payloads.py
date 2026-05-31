"""

from models.booking_model import (
    Booking,
    BookingDates
)

payload = Booking(
    firstname="John",
    lastname="Doe",
    totalprice=100,
    depositpaid=True,
    bookingdates=BookingDates(
        checkin="2025-01-01",
        checkout="2025-01-05"
    ),
    additionalneeds="Breakfast"
)

partial_payload = PartialBooking(

)
"""