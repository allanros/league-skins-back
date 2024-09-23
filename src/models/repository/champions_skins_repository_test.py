from .champions_skins_repository import ChampionsSkinsRepository

class CollectionMock:
    def __init__(self) -> None:
        self.insert_one_att = {}
        self.find_att = {}
        self.update_att = {}

    def insert_one(self, user: dict) -> None:
        self.insert_one_att["dict"] = user

    def find_one(self, *args):
        self.find_att["args"] = args

    def update_one(self, *args, **kwargs):
        self.update_att["args"] = args
        self.update_att["kwargs"] = kwargs

class DbConnectionMock:
    def __init__(self, collection) -> None:
        self.get_collection_att = {}
        self.collection = collection

    def get_collection(self, collection_name: str):
        self.get_collection_att["collection_name"] = collection_name

        return self.collection

def test_insert_champion():
    collection = CollectionMock()
    db_connection = DbConnectionMock(collection)
    repo = ChampionsSkinsRepository(db_connection)

    champion = {
        "champion": "Aatrox",
        "skins": [
            {
                "skin_id": "1",
                "name": "Justicar Aatrox",
                "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aatrox_1.jpg"
            },
            {
                "skin_id": "2",
                "name": "Mecha Aatrox",
                "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aatrox_2.jpg"
            }
        ]
    }

    repo.insert_champion(champion)

    assert collection.insert_one_att["dict"] == champion

def test_update_champion_skins():
    collection = CollectionMock()
    db_connection = DbConnectionMock(collection)
    repo = ChampionsSkinsRepository(db_connection)

    champion_name = "Aatrox"
    skins = [
        {
            "skin_id": "1",
            "name": "Justicar Aatrox",
            "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aatrox_1.jpg"
        },
        {
            "skin_id": "2",
            "name": "Mecha Aatrox",
            "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aatrox_2.jpg"
        },
        {
            "skin_id": "3",
            "name": "Blood Moon Aatrox",
            "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aatrox_3.jpg"
        }
    ]

    repo.update_champion_skins(champion_name, skins)

    assert collection.update_att["args"][0] == { "champion": champion_name }
    assert collection.update_att["args"][1] == { "$set": { "skins": skins } }
