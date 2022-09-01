## An Async Tasks -> Results Pattern ##
import random
import asyncio
import time

from httpx import AsyncClient

ADDRESSES = 'a b c d e'.split()

# When doing for loops, we commonly gather results with these patterns:
# 1. Empty List -> For Loops -> List append -> return List
# 2. For Loops -> Yield Function -> List Yields
# 3. List comprehension


def make_api_request_seq(client, addr):
    wait_time = random.uniform(0.1, 3)
    time.sleep(wait_time)  # random time needed to complete a request
    return f"{addr} - ({wait_time:.2f})"


def make_multiple_requests_seq():
    random.seed(1)
    t0 = time.perf_counter()
    results = [make_api_request_seq(None, addr) for addr in ADDRESSES]
    print(f"seq time - {(time.perf_counter() - t0)}")
    return results


# When doing async tasks, we don't need to do this.
# We can just use `gather` to grab all the results that are completed


async def make_api_request_async(client: AsyncClient, addr):
    wait_time = random.uniform(0.1, 3)
    await asyncio.sleep(wait_time)
    return f"{addr} - ({wait_time:.2f})"


async def supervisor():
    random.seed(1)
    async with AsyncClient() as client:
        # start async resquest with multiple requests endpoints
        to_do = [make_api_request_async(client, addr) for addr in ADDRESSES]

        # gather the results from async completion
        results = await asyncio.gather(*to_do)

    return results


# the main/ entry point of async func
def make_multiple_requests_async():
    t0 = time.perf_counter()
    results = asyncio.run(supervisor())
    print(f"async time - {(time.perf_counter() - t0)}")
    return results


if __name__ == '__main__':
    print(make_multiple_requests_seq())
    print('-' * 10)
    print(make_multiple_requests_async())
