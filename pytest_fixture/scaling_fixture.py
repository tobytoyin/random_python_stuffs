import pytest


### How fixture can improve test cases scale up
class Car:
    """Car V.1"""

    def __init__(self) -> None:
        self.engine_started = False

    def start_engine(self) -> None:
        self.engine_started = True
        return


@pytest.fixture
def car_default() -> Car:
    return Car()


@pytest.fixture
def car_start_engine() -> Car:
    car = Car()
    car.start_engine()
    return car


# A test case can have both
# we can test multiple scenarios at the same time
def test_car_engine(car_default, car_start_engine):
    # engine should not be started by default
    assert car_default.engine_started == False

    # engine should be started when a car started
    assert car_start_engine.engine_started == True


### When development scaled, the Car might have additional features,
# while we want to minimise code change of existing test cases

# Assume this is a newly merged code
class Car:
    """Car V.2"""

    def __init__(self) -> None:
        self.engine_started = False

    def start_engine(self) -> None:
        self.engine_started = True
        return

    # ++ a feature being added
    def stop_engine(self) -> None:
        self.engine_started = False
        return


@pytest.fixture
def car_default() -> Car:
    return Car()


@pytest.fixture
def car_start_engine() -> Car:
    car = Car()
    car.start_engine()
    return car


# ++ Extend our existing fixture test cases instead of rewriting them
@pytest.fixture
def stop_default_car(car_default):
    car_default.stop_engine()
    return car_default


@pytest.fixture
def stop_started_car(car_start_engine):
    car_start_engine.stop_engine()
    return car_start_engine


def test_car_engine(car_default, car_start_engine):
    assert car_default.engine_started == False
    assert car_start_engine.engine_started == True


# ++ adding in a new test cases
def test_engine_after_stop(stop_default_car, stop_started_car):
    assert stop_default_car.engine_started == False
    assert stop_started_car.engine_started == False
