from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.models.repository.interfaces.champions_skins_interface \
    import ChampionsSkinsRepositoryInterface

class ChampionFinder:
    def __init__(self, champion_repository: ChampionsSkinsRepositoryInterface) -> None:
        self.__champion_repo = champion_repository

    def find(self, http_request: HttpRequest) -> HttpResponse:
        try:
            champion_name = http_request.body["champion"]
            self.__validate_data(champion_name)

            champion_data = self.__find_champion(champion_name)

            return self.__format_response(champion_data)
        except Exception as e:
            return HttpResponse(
                status_code=500,
                body={
                    "message": str(e)
                }
            )

    def find_all(self) -> HttpResponse:
        try:
            champion_data = self.__champion_repo.find_champions()
            return self.__format_response(champion_data)
        except Exception as e:
            return HttpResponse(
                status_code=500,
                body={
                    "message": str(e)
                }
            )

    def __validate_data(self, champion_name: str) -> None:
        pass # need to implement

    def __find_champion(self, champion_name: str) -> dict:
        champion_data = self.__champion_repo.find_champion_skin(champion_name)
        if champion_data is None:
            raise Exception("Champion not found")
        return champion_data

    def __format_response(self, champion_data: dict) -> HttpResponse:
        return HttpResponse(
            body={
                "type": "champion",
                "count": 1,
                "success": True,
                "attributes": champion_data
            },
            status_code=200
        )
