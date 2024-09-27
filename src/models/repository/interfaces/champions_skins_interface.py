from abc import ABC, abstractmethod
from datetime import datetime

class ChampionsSkinsRepositoryInterface(ABC):
    @abstractmethod
    def insert_champion(self, champion_data: dict) -> None:
        pass

    @abstractmethod
    def update_champion_skins(self, champion_name: str, skins: list) -> None:
        pass

    @abstractmethod
    def insert_last_updated(self) -> None:
        pass

    @abstractmethod
    def insert_api_version(self, version: str) -> None:
        pass

    @abstractmethod
    def get_api_version(self) -> str:
        pass

    @abstractmethod
    def get_last_updated(self) -> datetime:
        pass

    @abstractmethod
    def find_champions(self) -> list:
        pass

    @abstractmethod
    def find_champion_skin(self, champion_name: str) -> list:
        pass
