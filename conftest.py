import pytest

from playwright.sync_api import sync_playwright

from core.api_client import APIClient
from services.auth_service import AuthService
from services.booking_service import BookingService
from config.config import Config


@pytest.fixture(scope="session")
def request_context():

    with sync_playwright() as playwright:
        request = playwright.request.new_context(
            base_url = Config.BASE_URL
        )

        yield request

        request.dispose()


@pytest.fixture
def api_client(request_context):

    return APIClient(request_context)


@pytest.fixture
def booking_service(api_client):

    return BookingService(api_client)


@pytest.fixture
def auth_service(api_client):

    return AuthService(api_client)