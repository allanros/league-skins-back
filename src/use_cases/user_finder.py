from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest
from src.models.repository.interfaces.users_repository_interface import UsersRepositoryInterface

class UserFinder:
    def __init__(self, user_repository: UsersRepositoryInterface) -> None:
        self.user_repo = user_repository

    def find(self, http_request: HttpRequest) -> HttpResponse:
        try:
            user_id = http_request.headers.get("User-ID")
            user = self.__find_user(user_id)

            return self.__format_response(user)

        except Exception as e:
            return HttpResponse(status_code=500, body={"message": str(e)})

    def __find_user(self, user_id: str) -> dict:
        user = self.user_repo.find_user_by_object_id(user_id)
        if user is None:
            raise Exception("User not found")
        return user

    def __format_response(self, user: dict) -> HttpResponse:
        user.pop("_id")
        return HttpResponse(
            status_code=200,
            body={
                "data": {
                    "type": "user",
                    "count": 1,
                    "attributes": user
                }
            }
        )
