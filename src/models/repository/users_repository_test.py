from bson import ObjectId
from .users_repository import UsersRepository

class CollectionMock:
    def __init__(self) -> None:
        self.insert_one_att = {}
        self.find_att = {}
        self.update_att = {}

    def insert_one(self, user: dict) -> None:
        self.insert_one_att["dict"] = user

    def find_one(self, *args):
        self.find_att["args"] = args

    def update_one(self, *args):
        self.update_att["args"] = args

class DbConnectionMock:
    def __init__(self, collection) -> None:
        self.get_collection_att = {}
        self.collection = collection

    def get_collection(self, collection_name: str):
        self.get_collection_att["collection_name"] = collection_name

        return self.collection

def test_insert_user():
    collection = CollectionMock()
    db_connection = DbConnectionMock(collection)
    repo = UsersRepository(db_connection)

    user = { "name": "test", "email": "teste@teste.com" }
    repo.insert_user(user)

    assert collection.insert_one_att["dict"] == user

def test_find_user_by_object_dict():
    collection = CollectionMock()
    db_connection = DbConnectionMock(collection)
    repo = UsersRepository(db_connection)

    user_id = "66edc569882a30414f607f02"
    repo.find_user_by_object_id(user_id)

    assert collection.find_att["args"] == ({ "_id": ObjectId(user_id) }, { "_id": 0 })

def test_update_user():
    collection = CollectionMock()
    db_connection = DbConnectionMock(collection)
    repo = UsersRepository(db_connection)

    user_id = "66edc569882a30414f607f02"
    user_data = { "name": "test2", "password": "123456" }

    repo.update_user(user_id, user_data)

    assert collection.update_att["args"] == ({ "_id": ObjectId(user_id) }, { "$set": user_data })

def test_add_user_skins():
    collection = CollectionMock()
    db_connection = DbConnectionMock(collection)
    repo = UsersRepository(db_connection)

    user_id = "66edc569882a30414f607f02"
    skins = [ "skin1", "skin2" ]

    repo.add_user_skins(user_id, skins)

    assert collection.update_att["args"] == ({ "_id": ObjectId(user_id) }, { "$push": { "skins": skins } })
