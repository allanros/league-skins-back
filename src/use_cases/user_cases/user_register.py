from datetime import datetime
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.models.repository.interfaces.users_repository_interface import UsersRepositoryInterface

class UserRegister:
    def __init__(self, user_repository: UsersRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def register(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body

            new_user = self.__format_new_user(body)
            self.__insert_user(new_user)

            return self.__format_response(new_user["username"])
        except Exception as e:
            return HttpResponse(
                status_code=500,
                body={
                    "error": str(e)
                }
            )

    def __insert_user(self, body: dict) -> None:
        self.__user_repository.insert_user(body)

    def __format_new_user(self, body: dict) -> dict:
        new_user = body["user"]
        new_user = { **new_user, "created_at": datetime.now() }
        return new_user

    def __format_response(self, username: str) -> HttpResponse:
        return HttpResponse(
            status_code=201,
            body={
                "data": {
                    "type": "user",
                    "success": True,
                    "attributes": {
                        "username" : username
                    }
                }
            }
        )
