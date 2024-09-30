from src.main.http_types.http_request import HttpRequest
from .champion_updater import ChampionFinder

class ChampionFinderMock:
    def __init__(self) -> None:
        self.champion_updater_att = {}

    def update_champion_skins(self, champion_name: str, champion_skins: list, version: str) -> None:
        self.champion_updater_att["champion_name"] = champion_name
        self.champion_updater_att["champion_skins"] = champion_skins
        self.champion_updater_att["version"] = version

def test_champion_updater():
    repo = ChampionFinderMock()
    champion_finder = ChampionFinder(repo)

    mock_request = HttpRequest(
        body={
            "champion": "Yasuo",
            "skins": [
                {
                    "skin_id": "1",
                    "name": "High Noon",
                    "image": "https://url.com"
                }
            ],
            "version": "11.1.1"
        }
    )

    response = champion_finder.update(mock_request)

    assert response.status_code == 200
    assert repo.champion_updater_att["champion_name"] == "Yasuo"
    assert repo.champion_updater_att["champion_skins"] == mock_request.body["skins"]
