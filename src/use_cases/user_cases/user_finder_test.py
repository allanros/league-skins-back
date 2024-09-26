from src.main.http_types.http_request import HttpRequest
from .user_finder import UserFinder

class UserFinderMock:
    def __init__(self) -> None:
        self.find_att = {}

    def find_user_by_object_id(self, user_id: str) -> dict:
        self.find_att["user_id"] = user_id
        return {
            "_id": "1",
            "username": "test"
        }

def test_user_finder():
    repo = UserFinderMock()
    user_finder = UserFinder(repo)

    mock_request = HttpRequest(headers={"User-ID": "66edc569882a30414f607f02"})

    user = user_finder.find(mock_request)

    assert user.body["data"]["attributes"]["username"] == "test"
    assert user.status_code == 200
    assert repo.find_att["user_id"] == mock_request.headers["User-ID"]
