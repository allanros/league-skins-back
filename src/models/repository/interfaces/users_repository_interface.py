from abc import ABC, abstractmethod

class UsersRepositoryInterface(ABC):
    @abstractmethod
    def insert_user(self, user: dict) -> None:
        pass

    @abstractmethod
    def find_user_by_object_id(self, user_id: str) -> dict:
        pass

    @abstractmethod
    def find_user_by_email(self, email: str) -> dict:
        pass

    @abstractmethod
    def update_user(self, user_id: str, user_data: dict) -> None:
        pass

    @abstractmethod
    def add_user_skins(self, user_id: str, skins: list) -> None:
        pass
