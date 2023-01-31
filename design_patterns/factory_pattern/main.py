from city import NewYork, CentralCity
from hero_factory import DCHeroFactory, MarvelHeroFactory


if __name__ == '__main__':
    # the "client" class can be reused and take in any Factory
    nyc = NewYork(factory=MarvelHeroFactory)
    nyc.run(preference='powerful')

    print('\n')

    # another client class can be created without rewriting everything
    # this is possible when we just pass another Factory into the class
    ccc = CentralCity(factory=DCHeroFactory)
    ccc.run(preference='fast')
