from src.main.http_types.http_response import HttpResponse
from src.models.repository.interfaces.champions_skins_interface \
    import ChampionsSkinsRepositoryInterface

class ChampionFinderPaged:
    def __init__(self, champion_repository: ChampionsSkinsRepositoryInterface) -> None:
        self.__champion_repo = champion_repository

    def find_paged(self, page: int = 0) -> HttpResponse:
        try:
            champion_data = list(self.__champion_repo.find_champions())
            total_pages = len(champion_data) // 10
            champion_data = champion_data[page * 10:page * 10 + 10]
            return self.__format_response(champion_data, total_pages)
        except Exception as e:
            return HttpResponse(
                status_code=500,
                body={
                    "message": str(e)
                }
            )

    def __format_response(self, champion_data: list, total_pages: int) -> HttpResponse:
        return HttpResponse(
            status_code=200,
            body={
                "type": "champions",
                "count": len(champion_data),
                "total_pages": total_pages,
                "attributes": champion_data
            }
       )
