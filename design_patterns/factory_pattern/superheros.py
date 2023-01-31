from abc import ABC, abstractmethod


class Superhero(ABC):
    @property
    @abstractmethod
    def name(self):
        NotImplementedError

    @abstractmethod
    def use_ability(self):
        NotImplementedError


# various kind of concrete Superheroes from DC verse
class Superman(Superhero):
    @property
    def name(self):
        return "Superman"

    def use_ability(self):
        return "punch"


class Batman(Superhero):
    @property
    def name(self):
        return "Batman"

    def use_ability(self):
        return "throw batarang"


class Flash(Superhero):
    @property
    def name(self):
        return "the Flash"

    def use_ability(self):
        return "run"


# various kind of concrete Superheros from Marvel verse
class DoctorStrange(Superhero):
    @property
    def name(self):
        return "Doctor Strange"

    def use_ability(self):
        return "magic"


class Hulk(Superhero):
    @property
    def name(self):
        return "Incredible Hulk"

    def use_ability(self):
        return "smash"


class SpiderMan(Superhero):
    @property
    def name(self):
        return "Spider-man"

    def use_ability(self):
        return "use spider web"


if __name__ == '__main__':
    print(Superman().use_ability())
