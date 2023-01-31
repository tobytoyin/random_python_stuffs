# A hero factory is a selection layer on which Superhero to assign
from abstract_classes import HeroFactory
import superheros

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
