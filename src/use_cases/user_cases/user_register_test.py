from src.main.http_types.http_request import HttpRequest
from .user_register import UserRegister

class UserRepositoryMock:
    def __init__(self) -> None:
        self.insert_user_att = {}

    def insert_user(self, user: dict) -> None:
        self.insert_user_att["user"] = user

class UserRepositoryMockError:
    def __init__(self) -> None:
        self.insert_user_att = {}

    def insert_user(self, user: dict) -> None:
        raise Exception("Error")

def test_user_register():
    repo = UserRepositoryMock()
    user_register = UserRegister(repo)

    mock_request = HttpRequest(
        body={
            "user": {
                "username": "test",
                "email" : "test@teste.com",
                "password": "123456"
            }
        }
    )

    response = user_register.register(mock_request)

    assert response.status_code == 201
    assert response.body["data"]["attributes"]["username"] == "test"

def test_user_register_error():
    repo = UserRepositoryMockError()
    user_register = UserRegister(repo)

    mock_request = HttpRequest(
        body={
            "user": {
                "username": "test",
                "email" : "test@teste.com",
                "password": "123456"
            }
        }
    )

    response = user_register.register(mock_request)

    assert response.status_code == 500
