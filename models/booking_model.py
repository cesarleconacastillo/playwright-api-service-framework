from typing import Optional

from pydantic import BaseModel, Field


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class Booking(BaseModel):

    firstname: str = Field(
        min_length=2,
        max_length=50
    )

    lastname: str = Field(
        min_length=2,
        max_length=50
    )

    totalprice: int = Field(gt=0)

    depositpaid: bool

    bookingdates: BookingDates

    additionalneeds: str


class PartialBooking(BaseModel):

    firstname: Optional[str] = Field(
        min_length=2,
        max_length=50
    )

    lastname: Optional[str] = Field(
        min_length=2,
        max_length=50
    )