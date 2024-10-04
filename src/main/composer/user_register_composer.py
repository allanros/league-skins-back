from src.models.repository.users_repository import UsersRepository
from src.use_cases.user_cases.user_register import UserRegister
from src.models.connection.connection_handler import db_connection_handler

def user_register_composer():
    connection = db_connection_handler.get_db_connection()
    model = UsersRepository(connection)
    use_case = UserRegister(model)

    return use_case
