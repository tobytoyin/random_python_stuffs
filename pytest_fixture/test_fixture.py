import pytest


# fixture some test data
@pytest.fixture
def get_some_numbers():
    return [1, 2, 3]


# fixture some test result
@pytest.fixture
def test_results():
    return [2, 3, 4]


# function to test
def add_one_to_all(*number: int):
    return list(map(lambda x: x + 1, number))


# test case
# The argument of the test function needs to be the same as the
# fixture function for PyTest to search for it
def test_add_one_to_all(get_some_numbers, test_results):
    assert add_one_to_all(*get_some_numbers) == test_results
