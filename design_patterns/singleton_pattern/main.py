from __future__ import annotations


class SingletonContext:
    class __SingletonClass:
        """SingletonClass is private and live inside the Context only.
        Therefore, it can only be instanciated and access within the Context
        """

        def __init__(self, name) -> None:
            self.name = name

        def some_logics(self):
            # class logics lives inside here
            pass

    __instance = None
    __name = None

    def __new__(cls, name: str) -> None:
        """Setup a Singleton launcher with input params"""
        cls.__name = name if not cls.__name else cls.__name

        return super().__new__(cls)  # return the class object

    @classmethod
    @property
    def name(cls):
        return cls.__name

    @classmethod
    def get_instance(cls) -> __SingletonClass:
        """Get or Create an instance of a Singleton Object"""
        if not cls.__instance:
            print(f"initialising instance : {cls.name}")
            cls.__instance = cls.__SingletonClass(name=cls.name)
        else:
            print(f"Found instance : {cls.name}")

        return cls.__instance


if __name__ == '__main__':
    # some tests that our singleton is working properly
    instance1 = SingletonContext('instance-1').get_instance()
    instance2 = SingletonContext('instance-1').get_instance()

    assert instance1 == instance2  # singleton objects
    assert instance1.name == instance2.name  # name are the same

    instance3 = SingletonContext('instance-3').get_instance()

    assert instance1 == instance3  # single objects even when name is different
    assert instance1.name == instance2.name  # defined name won't get changed
