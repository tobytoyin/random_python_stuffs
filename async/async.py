## We want to find all the cities that starts with "saint"
import json

import re
import asyncio
from time import perf_counter

with open('world_cities.json', 'rb') as f:
    CITIES = json.load(f)

# we can do this sequentially
def find_city_sequentially(regex):
    for city in CITIES:
        if re.search(regex, city['name']):
            yield (city['name'], city['country'])


def seq_main():
    results = list(find_city_sequentially('^Saint'))
    print(results[0:5])


# we can do this asynchronously
async def find_city_async(regex, city):
    if re.search(regex, city['name']):
        return (city['name'], city['country'])
    return False


async def async_main():
    # This passing in a list of coroutines for async to work on
    # which resemblence a queue of tasks for async to swap between
    # Essentially, the list run these Tasks:
    # city1 --> find_city_async --> result1 waiting to be retrieve
    # city2 --> find_city_async --> result2 waiting to be retrieve
    coros = [find_city_async('^Saint', city) for city in CITIES]

    # check each corountine and find out which Task is actually completed
    results = []
    for coro in asyncio.as_completed(coros):
        result = await coro
        results.append(result) if result else None

    print(results[0:5])


if __name__ == '__main__':
    seq_main()
    asyncio.run(async_main())
