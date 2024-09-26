from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest
from src.models.repository.interfaces.users_repository_interface import UsersRepositoryInterface

class UserAddSkin:
    def __init__(self, user_repository: UsersRepositoryInterface) -> None:
        self.__user_repo = user_repository

    def add(self, http_request: HttpRequest) -> HttpResponse:
        try:
            user_id = http_request.headers.get("User-ID")
            skin_data = http_request.body
            self.__validate_data(skin_data)

            self.__add_skin(user_id, skin_data)

            return self.__format_response()
        except Exception as e:
            return HttpResponse(
                status_code=500,
                body={
                    "message": str(e)
                }
            )

    def __add_skin(self, user_id: str, skins: list) -> None:
        user = self.__user_repo.find_user_by_object_id(user_id)
        if user is None:
            raise Exception("User not found")
        self.__user_repo.add_user_skins(user_id, skins)

    def __validate_data(self, skin_data: dict) -> None:
        pass

    def __format_response(self) -> HttpResponse:
        return HttpResponse(
            body={
                "type": "user_skins",
                "count": 1,
                "success": True
            },
            status_code=200
        )
