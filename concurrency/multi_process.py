import itertools
import time
from multiprocessing import Process, Event, synchronize


# The main Threading task, we need an Event to keep track of
# and synchronise different threading tasks
def brainstorming(done: Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\rThinking {char}'
        print(status, end='', flush=True)

        # wait for 0.1s, then check whether the Event is completed or not
        if done.wait(timeout=0.1):
            print("\r<end> Brainstorming Completed!", flush=True)
            break


def think_idea() -> str:
    time.sleep(3)
    print("\r> I got an idea")
    return "My brilliant idea"


def write_idea() -> str:
    print("\r> Write down some ideas")
    return


def multi_task_person() -> str:
    # Setup a brainstorming "done"
    done = Event()
    brainstorming = Process(target=brainstorming, args=(done,))
    print(f'<start> Brainstorming Start!')
    brainstorming.start()  # start the brainstorming at the "background"

    result = think_idea()
    _ = write_idea()

    done.set()
    brainstorming.join()

    return result


if __name__ == '__main__':
    result = multi_task_person()
    print(f"I said: '{result}'")
