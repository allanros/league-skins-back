from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.models.repository.interfaces.champions_skins_interface \
    import ChampionsSkinsRepositoryInterface

from src.validators.champion_updater_validator import champion_updater_validator

class ChampionFinder:
    def __init__(self, champion_repository: ChampionsSkinsRepositoryInterface) -> None:
        self.__champion_repo = champion_repository

    def update(self, http_request: HttpRequest) -> HttpResponse:
        try:
            self.__validate_data(http_request.body)
            champion_name = http_request.body["champion"]
            champion_skins = http_request.body["skins"]
            version = http_request.body["version"]

            self.__update_champion(champion_name, champion_skins, version)

            return self.__format_response()
        except Exception as e:
            return HttpResponse(
                status_code=500,
                body={
                    "message": str(e)
                }
            )

    def __validate_data(self, champion_skins: list) -> None:
        champion_updater_validator(champion_skins)

    def __update_champion(self, champion_name: str, champion_skins: list, version: str) -> None:
        self.__champion_repo.insert_api_version(version)
        self.__champion_repo.update_champion_skins(champion_name, champion_skins)

    def __format_response(self) -> HttpResponse:
        return HttpResponse(
            body={
                "type": "champion",
                "count": 1,
                "success": True
            },
            status_code=200
        )
