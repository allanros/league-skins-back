from src.main.http_types.http_request import HttpRequest
from .champion_finder import ChampionFinder

class ChampionFinderMock:
    def __init__(self) -> None:
        self.champion_finder_att = {}

    def find_champion_skin(self, champion_name: str) -> dict:
        self.champion_finder_att["champion_name"] = champion_name
        return {
            "skins": [
                {
                    "name": "default",
                    "id": 0
                },
                {
                    "name": "skin1",
                    "id": 1
                }
            ]
        }

    def find_champions(self) -> dict:
        self.champion_finder_att["champions"] = True
        return {
            "champions": [
                {
                    "name": "Aatrox",
                    "id": 266
                },
                {
                    "name": "Ahri",
                    "id": 103
                }
            ]
        }

    def get_api_version(self) -> str:
        return "1.0.0"

def test_champion_finder():
    repo = ChampionFinderMock()
    champion_finder = ChampionFinder(repo)

    mock_request = HttpRequest(body={"champion": "Aatrox"})

    response = champion_finder.find(mock_request)

    assert response.status_code == 200
    assert repo.champion_finder_att["champion_name"] == mock_request.body["champion"]

def test_champion_find_all():
    repo = ChampionFinderMock()
    champion_finder = ChampionFinder(repo)

    response = champion_finder.find_all()

    assert response.status_code == 200
    assert repo.champion_finder_att["champions"] is True
    assert response.body["attributes"]["champions"][0]["name"] == "Aatrox"
