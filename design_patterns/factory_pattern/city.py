from hero_factory import HeroFactory
from abc import ABC, abstractmethod

# Our "Client" class is a `City`
# which execute the main programme, i.e., request a hero and do something
# the good thing about a factory_pattern is that,
# this class no longer needs to know how choices of Heros classes are available

# It is interfaced and communicate with HeroFactory only
# which it handles all the detail


class City(ABC):
    def __init__(self, factory: HeroFactory) -> None:
        self.factory: HeroFactory = factory()
        super().__init__()

    @property
    @abstractmethod
    def name(self):
        NotImplementedError

    def _get_situation(self):
        print(f"{self.name} is having problem ...")

    def _request_hero(self, preference):
        hero = self.factory.create_hero(preference)
        print(f"Request for {hero.name}")
        print(f"{hero.name} uses {hero.use_ability()} to solve the problem")

    def run(self, preference):
        self._get_situation()
        self._request_hero(preference)
        return


class CentralCity(City):
    @property
    def name(self):
        return "Central City"


class NewYork(City):
    @property
    def name(self):
        return "New York City"
