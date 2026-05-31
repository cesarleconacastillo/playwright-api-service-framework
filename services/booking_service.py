from pydantic import BaseModel

from core.request_builder import RequestBuilder

class BookingService:

    def __init__(self, api_client):
        self.client = api_client

    def create_booking(self, booking):

        return self.client.post(
            "/booking",
            booking.model_dump()
        )

    def get_booking(self, booking_id):

        return self.client.get(
            f"/booking/{booking_id}"
        )

    def partial_booking_update(self, booking_id, booking, token):

        return self.client.patch(
            f"/booking/{booking_id}",
            booking.model_dump(),
            headers = RequestBuilder.auth_headers(token)
        )

    def full_booking_update(self, booking_id, booking, token):

        return self.client.put(
            f"/booking/{booking_id}",
            booking.model_dump(),
            headers = RequestBuilder.auth_headers(token)
        )

    def delete_booking(self, booking_id, token):

        return self.client.delete(
            f"/booking/{booking_id}",
            headers = RequestBuilder.auth_headers(token)
        )