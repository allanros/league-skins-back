from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest
from src.models.repository.interfaces.users_repository_interface import UsersRepositoryInterface

class UserUpdater:
    def __init__(self, user_repository: UsersRepositoryInterface) -> None:
        self.__user_repo = user_repository

    def update(self, http_request: HttpRequest) -> dict:
        try:
            user_id = http_request.headers.get("User-ID")
            user_data = http_request.body
            self.__validate_data(user_data)

            self.__update_user(user_id, user_data)

            return self.__format_response()
        except Exception as e:
            return HttpResponse(
                status_code=500,
                body={
                    "message": str(e)
                }
            )

    def __update_user(self, user_id: str, user_data: dict) -> dict:
        user = self.__user_repo.find_user_by_object_id(user_id)
        if user is None:
            raise Exception("User not found")
        self.__user_repo.update_user(user_id, user_data)

    def __validate_data(self, user_data: dict) -> dict:
        pass

    def __format_response(self) -> HttpResponse:
        return HttpResponse(
            body={
                "type": "user",
                "count": 1,
                "success": True
            },
            status_code=200
        )
