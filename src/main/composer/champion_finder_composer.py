from src.models.repository.champions_skins_repository import ChampionsSkinsRepository
from src.use_cases.champion_cases.champion_finder import ChampionFinder
from src.models.connection.connection_handler import db_connection_handler

def champion_finder_composer():
    connection = db_connection_handler.get_db_connection()
    model = ChampionsSkinsRepository(connection)
    use_case = ChampionFinder(model)

    return use_case
