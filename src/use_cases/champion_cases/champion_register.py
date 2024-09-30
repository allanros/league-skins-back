from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.models.repository.interfaces.champions_skins_interface \
    import ChampionsSkinsRepositoryInterface
from src.validators.champion_register_validator import champion_register_validator

class ChampionRegister:
    def __init__(self, champion_repository: ChampionsSkinsRepositoryInterface) -> None:
        self.__champion_repo = champion_repository

    def register(self, http_request: HttpRequest) -> HttpResponse:
        try:
            self.__validate_data(http_request.body)
            champion_data = http_request.body["data"]
            version = http_request.body["version"]

            self.__register_champion(champion_data, version)

            return self.__format_response()
        except Exception as e:
            return HttpResponse(
                status_code=500,
                body={
                    "message": str(e)
                }
            )

    def __validate_data(self, champion_data: dict) -> None:
        champion_register_validator(champion_data)

    def __register_champion(self, champion_data: dict, version: str) -> None:
        self.__champion_repo.insert_champion(champion_data)
        self.__champion_repo.insert_api_version(version)
        self.__champion_repo.insert_last_updated()

    def __format_response(self) -> HttpResponse:
        return HttpResponse(
            body={
                "type": "champion",
                "count": 1,
                "success": True
            },
            status_code=201
       )
