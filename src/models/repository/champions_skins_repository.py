from datetime import datetime
from .interfaces.champions_skins_interface import ChampionsSkinsRepositoryInterface

class ChampionsSkinsRepository(ChampionsSkinsRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__collection_name = "champions"
        self.__db_connection = db_connection

    def insert_champion(self, champion_data: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(champion_data)

    def insert_last_updated(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one({},{ "$set": {"last_updated": datetime.now()} }, upsert=True)

    def get_last_updated(self) -> datetime:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({}, {"_id": 0, "last_updated": 1})

        return data["last_updated"]

    def update_champion_skins(self, champion_name: str, skins: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one({ "champion": champion_name }, { "$set": { "skins": skins } })

    def insert_api_version(self, version: str) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one({}, {"$set": {"api_version": version}}, upsert=True)

    def get_api_version(self) -> str:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({}, {"_id": 0, "api_version": 1})

        return data["api_version"]

    def find_champions(self) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({}, {"_id": 0, "champion": 1, "skins": 1})

        return data

    def find_champion_skin(self, champion_name: str) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one(
            { "champion": champion_name },
            {"_id": 0, "champion": 1, "skins": 1}
        )

        return data
