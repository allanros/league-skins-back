from src.models.repository.champions_skins_repository import ChampionsSkinsRepository
from src.use_cases.champion_cases.champion_updater import ChampionUpdater
from src.models.connection.connection_handler import db_connection_handler

def champion_updater_composer():
    connection = db_connection_handler.get_db_connection()
    model = ChampionsSkinsRepository(connection)
    use_case = ChampionUpdater(model)

    return use_case
