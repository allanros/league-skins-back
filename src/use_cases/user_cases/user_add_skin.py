from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest
from src.models.repository.interfaces.users_repository_interface import UsersRepositoryInterface
from src.validators.user_add_skin_validator import user_add_skin_validator

class UserAddSkin:
    def __init__(self, user_repository: UsersRepositoryInterface) -> None:
        self.__user_repo = user_repository

    def add(self, http_request: HttpRequest) -> HttpResponse:
        try:
            user_id = http_request.headers.get("User-ID")
            skin_data = http_request.body
            self.__validate_data(skin_data)
            skin_data = skin_data.get("skin")

            self.__add_skin(user_id, skin_data)

            return self.__format_response(skin=skin_data)
        except Exception as e:
            return HttpResponse(
                status_code=500,
                body={
                    "message": str(e)
                }
            )

    def __add_skin(self, user_id: str, skin: str) -> None:
        user = self.__user_repo.find_user_by_object_id(user_id)
        if user is None:
            raise Exception("User not found")
        self.__user_repo.toggle_user_skins(user_id, skin)

    def __validate_data(self, skin_data: dict) -> None:
        user_add_skin_validator(skin_data)

    def __format_response(self, skin: str) -> HttpResponse:
        return HttpResponse(
            body={
                "type": "user_skins",
                "success": True,
                "attributes": skin
            },
            status_code=200
        )
