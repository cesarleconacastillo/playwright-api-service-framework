from test_data.auth_factory import AuthFactory


def test_generate_auth_token(
        auth_service
):

    auth_request = AuthFactory.create()

    response = auth_service.get_token(
           auth_request
    )

    assert response.status == 200, (
        f"Expected 200 but got {response.status}"
    )

    # Convert response to JSON
    response_body = response.json()
    print(response_body)

    assert "token" in response_body
    assert response_body["token"] is not None
    assert len(response_body["token"]) > 0