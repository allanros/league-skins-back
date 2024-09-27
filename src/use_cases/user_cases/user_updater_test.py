from src.main.http_types.http_request import HttpRequest
from .user_updater import UserUpdater

class UserRepositoryMock:
    def __init__(self) -> None:
        self.find_user_by_object_id_att = {}
        self.update_user_att = {}

    def find_user_by_object_id(self, user_id: str) -> dict:
        self.find_user_by_object_id_att["user_id"] = user_id
        return {"_id": user_id }

    def update_user(self, user_id: str, user: dict) -> None:
        self.update_user_att["user_id"] = user_id
        self.update_user_att["user"] = user

def test_user_updater():
    repo = UserRepositoryMock()
    user_updater = UserUpdater(repo)

    mock_request = HttpRequest(
        headers={
            "User-ID": "66edc569882a30414f607f02"
        },
        body={
            "user": {
                "email": "test2",
                "username": "test1"
            }
        }
    )

    response = user_updater.update(mock_request)

    assert response.status_code == 200
    assert repo.find_user_by_object_id_att["user_id"] == mock_request.headers["User-ID"]
    assert repo.update_user_att["user_id"] == mock_request.headers["User-ID"]
    assert repo.update_user_att["user"]["user"] == mock_request.body["user"]
