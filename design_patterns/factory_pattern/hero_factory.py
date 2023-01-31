from abc import ABC, abstractmethod
from typing import Dict
import superheros


# A hero factory is a selection layer on which Superhero to assign
class HeroFactory(ABC):
    @property
    @abstractmethod
    def preference_map(self) -> Dict[str, superheros.Superhero]:
        NotImplementedError

    def create_hero(self, preference: str) -> superheros.Superhero:
        # retrieve the Superhero are create an instance of it
        return self.preference_map.get(preference)()


# DC Verse HeroFactory
class DCHeroFactory(HeroFactory):
    @property
    def preference_map(self):
        return {
            'crime': superheros.Batman,
            'powerful': superheros.Superman,
            'fast': superheros.Flash,
        }


# Marvel Verse HeroFactory
class MarvelHeroFactory(HeroFactory):
    @property
    def preference_map(self):
        return {
            'powerful': superheros.DoctorStrange,
            'friendly': superheros.SpiderMan,
            'strong': superheros.Hulk,
        }


if __name__ == '__main__':
    # test a factory
    marvel_factory = MarvelHeroFactory()
    hero = marvel_factory.create_hero('powerful')
    print(f"Selected Hero is {hero.name} and can {hero.use_ability()}")
