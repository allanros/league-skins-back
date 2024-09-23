from datetime import datetime
from .interfaces.champions_skins_interface import ChampionsSkinsRepositoryInterface

class ChampionsSkinsRepository(ChampionsSkinsRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__collection_name = "champions"
        self.__db_connection = db_connection

    def insert_champion(self, champion_data: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        self.__insert_last_updated()
        collection.insert_one(champion_data)

    def __insert_last_updated(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one({},{ "$set": {"last_updated": datetime.now()} }, upsert=True)

    def update_champion_skins(self, champion_name: str, skins: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        self.__insert_last_updated()
        collection.update_one({ "champion": champion_name }, { "$set": { "skins": skins } })

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
