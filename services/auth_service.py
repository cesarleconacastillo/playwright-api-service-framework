class AuthService:

    def __init__(self, api_client):
        self.client = api_client

    def get_token(self, auth_request):

        return self.client.post(
            "/auth",
            auth_request.model_dump()
        )