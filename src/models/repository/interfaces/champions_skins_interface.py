from abc import ABC, abstractmethod

class ChampionsSkinsRepositoryInterface(ABC):
    @abstractmethod
    def insert_champion(self, champion_data: dict) -> None:
        pass

    @abstractmethod
    def update_champion_skins(self, champion_name: str, skins: list) -> None:
        pass

    @abstractmethod
    def find_champions(self) -> list:
        pass

    @abstractmethod
    def find_champion_skin(self, champion_name: str) -> list:
        pass
