from src.main.http_types.http_request import HttpRequest
from .user_add_skin import UserAddSkin

class UserRepositoryMock:
    def __init__(self) -> None:
        self.find_user_by_object_id_att = {}
        self.add_user_skins_att = {}

    def find_user_by_object_id(self, user_id: str) -> dict:
        self.find_user_by_object_id_att["user_id"] = user_id
        return {"_id": user_id}

    def add_user_skins(self, user_id: str, skins: list) -> None:
        self.add_user_skins_att["user_id"] = user_id
        self.add_user_skins_att["skins"] = skins

def test_user_add_skin():
    repo = UserRepositoryMock()
    user_add_skin = UserAddSkin(repo)

    mock_request = HttpRequest(
        headers={
            "User-ID": "66edc569882a30414f607f02"
        },
        body={
            "skins": [
                "Aatrox_1",
                "Aatrox_2",
                "Jayce_1"
            ]
        }
    )

    response = user_add_skin.add(mock_request)

    assert response.status_code == 200
    assert repo.find_user_by_object_id_att["user_id"] == mock_request.headers["User-ID"]
    assert repo.add_user_skins_att["user_id"] == mock_request.headers["User-ID"]
    assert repo.add_user_skins_att["skins"]["skins"] == mock_request.body["skins"]

def test_user_add_skin_error():
    repo = UserRepositoryMock()
    user_add_skin = UserAddSkin(repo)

    mock_request = HttpRequest(
        headers={
            "User-ID": "66edc569882a30414f607f02"
        },
        body={
            "skinsss": [
                "Aatrox_1",
                "Aatrox_2",
                "Jayce_1"
            ]
        }
    )


    response = user_add_skin.add(mock_request)
    print(response.body)

    assert response.status_code == 500
