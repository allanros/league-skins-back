from flask_jwt_extended import create_access_token
from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest
from src.models.repository.interfaces.users_repository_interface import UsersRepositoryInterface
from src.drivers.password_handler import PasswordHandler

class UserLogin:
    def __init__(self, user_repository: UsersRepositoryInterface):
        self.__user_repository = user_repository
        self.__password_handler = PasswordHandler()

    def login(self, http_request: HttpRequest) -> HttpResponse:
        try:
            user_email = http_request.body["email"]
            user_password = http_request.body["password"]

            user = self.__get_user(user_email)
            self.__validate_password(user_password, user["hashed_password"])

            access_token = self.__create_access_token(user)

            return self.__format_response(access_token)

        except Exception as e:
            return HttpResponse(
                status_code=500,
                body={
                    "error": str(e)
                }
            )

    def __get_user(self, email: str) -> dict:
        user = self.__user_repository.find_user_by_email(email)
        if user is None:
            raise Exception("User not found")

        return user

    def __validate_password(self, password: str, hashed_password: str) -> None:
        verify_password = self.__password_handler.check_password(password, hashed_password)
        if not verify_password:
            raise Exception("Invalid password")

    def __create_access_token(self, user: dict) -> str:
        user["_id"] = str(user["_id"])
        access_token = create_access_token(identity=user["_id"])
        return access_token

    def __format_response(self, access_token: str) -> HttpResponse:
        return HttpResponse(
            status_code=200,
            body={
                "data": {
                    "type": "user",
                    "success": True,
                    "attributes": {
                        "access_token" : access_token
                    }
                }
            }
        )
