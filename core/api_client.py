from playwright.sync_api import APIRequestContext


class APIClient:

    def __init__(self, request_context: APIRequestContext):
        self.request = request_context


    def get(self, endpoint, headers=None):

        return self.request.get(
            endpoint,
            headers=headers
        )


    def post(self, endpoint, payload):

        return self.request.post(
            endpoint,
            data = payload
        )


    def patch(self, endpoint, payload, headers=None):

        return self.request.patch(
            endpoint,
            data = payload,
            headers=headers
        )

    def put(self, endpoint, payload, headers=None):

        return self.request.put(
            endpoint,
            data = payload,
            headers=headers
        )


    def delete(self, endpoint, headers=None):
        return self.request.delete(
            endpoint,
            headers=headers
        )
