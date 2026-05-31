from faker import Faker

from models.booking_model import (
    Booking,
    PartialBooking,
    BookingDates
)

fake = Faker()


class BookingFactory:

    @staticmethod
    def create():

        return Booking(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            totalprice=100,
            depositpaid=True,
            bookingdates=BookingDates(
                checkin="2025-01-01",
                checkout="2025-01-05"
            ),
            additionalneeds="Breakfast"
        )


    @staticmethod
    def partial_update():
        return PartialBooking(
            firstname=fake.first_name(),
            lastname=fake.last_name()
        )

