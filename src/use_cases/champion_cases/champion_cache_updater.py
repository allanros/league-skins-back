from src.main.http_types.http_response import HttpResponse
from src.models.repository.interfaces.champions_skins_interface \
    import ChampionsSkinsRepositoryInterface

from src.utils.get_champions_riot_api import get_champions_from_riot_api
from src.utils.get_riot_api import get_version_comparision
from src.utils.get_champion_skins import get_champion_skins
from src.validators.champion_register_validator import champion_register_validator

class ChampionCacheUpdater:
    def __init__(self, champion_repository: ChampionsSkinsRepositoryInterface) -> None:
        self.__champion_repo = champion_repository

    def update_cache(self) -> HttpResponse:
        try:
            api_version_on_db = self.__get_api_version_on_db()
            last_version_api = self.__get_last_version_riot_api(api_version_on_db)
            if last_version_api["status"]:
                return HttpResponse(
                    status_code=200,
                    body={
                        "message": "Cache is up to date"
                    }
                )

            latest_version = last_version_api["last_version"]

            champions_on_api = sorted(set(self.__get_riot_champions(latest_version)))

            for champion in champions_on_api:
                champion_data = get_champion_skins(champion, latest_version)

                if not champion_data:
                    continue

                champion_skins_count = len(champion_data["data"]["skins"])
                champion_skins_on_db = self.__get_champion_skins_on_db(
                    champion_data["data"]["niceName"]
                )

                if champion_skins_count == champion_skins_on_db:
                    continue

                self.__validate_data(champion_data)
                self.__register_champion(champion_data["data"], latest_version)

            self.__champion_repo.insert_api_version(latest_version)
            return self.__format_response()


        except Exception as e:
            return HttpResponse(
                status_code=500,
                body={
                    "message": str(e)
                }
            )

    def __get_api_version_on_db(self) -> str:
        api_version = self.__champion_repo.get_api_version()

        return api_version

    def __get_last_version_riot_api(self, api_version: str) -> dict:
        return get_version_comparision(api_version)

    def __get_riot_champions(self, last_version: str) -> list:
        return get_champions_from_riot_api(last_version)

    def __get_champion_skins_on_db(self, champion_name: str) -> int:
        champion_data = self.__champion_repo.find_champion_skin(champion_name)
        if not champion_data:
            return 0

        return len(champion_data.get("skins", []))

    def __register_champion(self, champion_data: dict, version: str) -> None:
        self.__champion_repo.insert_champion(champion_data)
        self.__champion_repo.insert_api_version(version)
        self.__champion_repo.insert_last_updated()

    def __validate_data(self, champion_data: dict) -> None:
        champion_register_validator(champion_data)

    def __format_response(self) -> HttpResponse:
        return HttpResponse(
            status_code=200,
            body={
                "message": "Cache updated"
            }
        )
