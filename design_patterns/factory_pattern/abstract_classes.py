# A hero factory is a selection layer on which Superhero to assign
from abc import ABC, abstractmethod
from typing import Dict


class Superhero(ABC):
    @property
    @abstractmethod
    def name(self):
        NotImplementedError

    @abstractmethod
    def use_ability(self):
        NotImplementedError


class HeroFactory(ABC):
    @property
    @abstractmethod
    def preference_map(self) -> Dict[str, Superhero]:
        NotImplementedError

    def create_hero(self, preference: str) -> Superhero:
        # retrieve the Superhero are create an instance of it
        return self.preference_map.get(preference)()


class City(ABC):
    def __init__(
        self,
    ) -> None:
        super().__init__()
