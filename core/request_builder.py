class RequestBuilder:

    @staticmethod
    def auth_headers(token):

        return {
            "Cookie": f"token={token}"
        }

    @staticmethod
    def json_headers():

        return {
            "Content-Type": "application/json"
        }