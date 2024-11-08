from bson import ObjectId
from .interfaces.users_repository_interface import UsersRepositoryInterface

class UsersRepository(UsersRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__collection_name = "users"
        self.__db_connection = db_connection

    def insert_user(self, user: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(user)

    def find_user_by_object_id(self, user_id: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({ "_id": ObjectId(user_id) }, { "_id": 0, "hashed_password": 0 })

        return data

    def find_user_by_email(self, email: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({ "email": email }, {})

        return data

    def update_user(self, user_id: str, user_data: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one({ "_id": ObjectId(user_id) }, { "$set": user_data })

    def toggle_user_skins(self, user_id: str, skin: str) -> None:
        user = self.find_user_by_object_id(user_id)
        skins = user.get("skins", [])
        collection = self.__db_connection.get_collection(self.__collection_name)
        if skin in skins:
            collection.update_one(
                { "_id": ObjectId(user_id) },
                { "$pull": { "skins": skin } }
            )
        else:
            collection.update_one(
                { "_id": ObjectId(user_id) },
                { "$push": { "skins": skin } }
            )
