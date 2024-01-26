from abc import ABC, abstractmethod


class Character(ABC):
    """Class Character"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Character constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Character die method"""
        pass


class Stark(Character):
    """Stark Class"""

    def die(self):
        """Stark die method"""
        if self.is_alive:
            self.is_alive = False
