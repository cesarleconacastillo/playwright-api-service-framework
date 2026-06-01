import allure

from test_data.auth_factory import AuthFactory

@allure.feature("Booking")
@allure.story("Generate Token")
@allure.severity(
    allure.severity_level.CRITICAL
)
def test_generate_auth_token(
        auth_service
):
    with allure.step(
            "Generate authentication token"
    ):
        auth_request = AuthFactory.create()


    with allure.step(
            "Generate token"
    ):


        response = auth_service.get_token(
           auth_request
        )

    with allure.step(
            "Validate token response"
    ):

        assert response.status == 200, (
            f"Expected 200 but got {response.status}"
        )

        # Convert response to JSON
        response_body = response.json()


    assert "token" in response_body
    assert response_body["token"] is not None
    assert len(response_body["token"]) > 0