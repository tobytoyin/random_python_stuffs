from typing import Union
from functools import singledispatch

# when a function is dealing with different Types
# it would easily become very messy:
def make_number(n: Union[str, float, int]) -> int:
    if isinstance(n, int):
        return n
    if isinstance(n, str):
        try:
            return int(n)
        except ValueError:
            return None

    if isinstance(n, float):
        return int(round(n))

    return None


# a singledispatch function is useful to:
# - keep the function namespace the same
# - 'dispatch' different Types handling into separate functions -> more maintainable
# - function becomes "generic", i.e., accept Types as parameter and response differently

# although our script contains more functions
# but each function is now much simpler and handle one thing only
# this makes it easier to add more logics in between without making a single func too lengthy
@singledispatch
def make_number_v2(n) -> int:
    """generic function"""
    return None


@make_number_v2.register
def _(n: int) -> int:
    """make_number when n is int type"""
    # add more stuff
    return n


@make_number_v2.register
def _(n: str) -> int:
    """make_number when n is str type"""
    try:
        return int(n)
    except ValueError:
        return None


@make_number_v2.register
def _(n: float) -> int:
    """make_number when n is float type"""
    # add more stuff
    return int(round(n))


if __name__ == '__main__':
    numbers = [10, '5', 11.4, False, '?', [1, 2, 3]]

    print(list(map(make_number, numbers)))

    print(list(map(make_number_v2, numbers)))
