from src.models.repository.champions_skins_repository import ChampionsSkinsRepository
from src.use_cases.champion_cases.champion_register import ChampionRegister
from src.models.connection.connection_handler import db_connection_handler

def champion_register_composer():
    connection = db_connection_handler.get_db_connection()
    model = ChampionsSkinsRepository(connection)
    use_case = ChampionRegister(model)

    return use_case
