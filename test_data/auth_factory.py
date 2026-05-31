from config.config import Config

from models.auth_model import AuthRequest


class AuthFactory:

    @staticmethod
    def create():

        return AuthRequest(
            username=Config.AUTH_USER,
            password=Config.AUTH_PWD
        )