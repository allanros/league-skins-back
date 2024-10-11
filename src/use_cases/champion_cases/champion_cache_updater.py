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

            champions_on_api = self.__get_riot_champions(last_version_api["last_version"])
            champions_on_db = self.__get_champions_on_db()

            diff_champions = sorted(set(champions_on_api) - set(champions_on_db))

            if not diff_champions:
                return HttpResponse(
                    status_code=200,
                    body={
                        "message": "Cache is up to date"
                    }
                )

            latest_version = last_version_api["last_version"]

            count = 0

            for champion in diff_champions:
                champion_data = get_champion_skins(champion, latest_version)
                self.__validate_data(champion_data)
                self.__register_champion(champion_data["data"], latest_version)
                count += 1
                if count == 10:
                    break

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
        if not api_version:
            return ""

        return api_version

    def __get_last_version_riot_api(self, api_version: str) -> dict:
        return get_version_comparision(api_version)

    def __get_riot_champions(self, last_version: str) -> list:
        return get_champions_from_riot_api(last_version)

    def __get_champions_on_db(self) -> list:
        champions = list(self.__champion_repo.find_champions())
        if not champions[0]:
            print("No champions found on db")
            return []

        names = []

        for champion in champions:
            names.append(champion["niceName"])

        return names

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
