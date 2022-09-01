import asyncio
import itertools
import time


async def brainstorming() -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\rThinking {char}'
        print(status, end='', flush=True)

        # wait for 0.1s, then check whether the Event is completed or not
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            print("\r<end> Brainstorming Completed!", flush=True)
            break


async def think_idea() -> str:
    await asyncio.sleep(3)
    print("\r> I got an idea")
    return "My brilliant idea"


async def write_idea() -> str:
    print("\r> Write down some ideas")
    return


async def supervisor():
    brainstorm_session = asyncio.create_task(brainstorming())

    result = await think_idea()
    _ = await write_idea()

    brainstorm_session.cancel()

    return result


def main() -> None:
    result = asyncio.run(supervisor())
    print(f"I said: '{result}'")


if __name__ == '__main__':
    main()
