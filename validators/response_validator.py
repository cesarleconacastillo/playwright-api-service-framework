class ResponseValidator:

    @staticmethod
    def verify_status(
        response,
        expected
    ):
        assert response.status == expected