from src.main.http_types.http_request import HttpRequest
from .champion_register import ChampionRegister

class UserRepositoryMock:
    def __init__(self) -> None:
        self.champions_insert_att = {}

    def insert_champion(self, champion_data: dict) -> None:
        self.champions_insert_att["champion"] = champion_data

    def insert_api_version(self, version: str) -> None:
        self.champions_insert_att["version"] = version

    def insert_last_updated(self) -> None:
        self.champions_insert_att["last_updated"] = True

def test_register():
    repo = UserRepositoryMock()
    champion_register = ChampionRegister(repo)

    mock_request = HttpRequest(
        body={
            "data": {
                "champion": "Aatrox",
                "niceName": "Aatrox",
                "skins": [
                    {
                        "skin_id": "1",
                        "name": "Justicar Aatrox",
                        "image": "justicar_aatrox.jpg"
                    },
                    {
                        "skin_id": "2",
                        "name": "Mecha Aatrox",
                        "image": "mecha_aatrox.jpg"
                    }
                ]
            },
            "version": "1.0.0"
        }
    )

    response = champion_register.register(mock_request)

    assert response.status_code == 201
    assert response.body["type"] == "champion"
    assert repo.champions_insert_att["champion"] == mock_request.body["data"]
    assert repo.champions_insert_att["version"] == mock_request.body["version"]
    assert repo.champions_insert_att["last_updated"] is True
