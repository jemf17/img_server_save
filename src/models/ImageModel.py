from __future__ import annotations
from abc import ABC, abstractmethod

class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

class Strategy(ABC):

    @abstractmethod
    async def add(self, user_id: int, user_data: dict):
        pass
    @abstractmethod
    async def update(self, user_id: int, user_data: dict):
        pass
    @abstractmethod
    async def delete(self, user_id: int):
        pass
    @abstractmethod
    async def get   (self, user_id: int):
        pass


class ScanModel(Strategy):
    @classmethod
    async def add(self, user_id: int, user_data: dict):
        try:
            pass
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None
    @classmethod
    async def update(self, user_id: int, user_data: dict):
        try:
            pass
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None
    @classmethod
    async def delete(self, user_id: int):
        try:
            pass
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None
    @classmethod
    async def get   (self, user_id: int):
        try:
            pass
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None
        
class ObraModel(Strategy):
    @classmethod
    async def add(self, user_id: int, user_data: dict):
        try:
            pass
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None
    @classmethod
    async def update(self, user_id: int, user_data: dict):
        try:
            pass
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None
    @classmethod
    async def delete(self, user_id: int):
        try:
            pass
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None
    @classmethod
    async def get   (self, user_id: int):
        try:
            pass
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None