import sys
from multiprocessing import SimpleQueue, Process
from multiprocessing import queues
import random

MATERIALS = ['apple', 'orange', 'pineapple', 'strawberry']
POISON_PILL = '<end>'

# data types
MaterialQueue = queues.SimpleQueue[str]
BakeryQueue = queues.SimpleQueue[str]


def make_bread(material: str) -> str:
    bakery = random.choice(['cake', 'bread', 'muffin'])
    return f"{material} {bakery}"


def worker(materials: MaterialQueue, results: BakeryQueue):
    # continously do the job until the queue is pruned
    while (material := materials.get()) != POISON_PILL:
        results.put(make_bread(material))

    results.put(POISON_PILL)  # insert poison pill for next queue


def start_bakery(
    num_workers: int,
    materials: MaterialQueue,
    results: BakeryQueue,
) -> None:
    # this would not return anything because the results are return back to the
    # mutable queues which provided by the arguments

    # put these materials into the MaterialQueue as materials
    rand_materials = random.choices(MATERIALS, k=10)
    for material in rand_materials:
        materials.put(material)

    # generate multiple number of workers, i.e., Process
    for _ in range(num_workers):
        worker_ = Process(target=worker, args=(materials, results))
        worker_.start()
        materials.put(POISON_PILL)


def stock_bakery(num_workers, results: BakeryQueue):
    worker_done = 0
    while worker_done < num_workers:
        while (result := results.get()) != POISON_PILL:
            yield result
        worker_done += 1


def main() -> None:
    # read in input command
    num_workers = int(sys.argv[1]) if len(sys.argv) >= 2 else 2

    # setup the queues for our bakery works
    # these are the external states for different processes to interact with
    materials: MaterialQueue = SimpleQueue()
    results: BakeryQueue = SimpleQueue()

    # start the materials queue (dequeue MaterialQueue)
    start_bakery(num_workers, materials, results)

    # start to stock the results (dequeue ResultsQueue)
    stocks = stock_bakery(num_workers, results)
    print("Bakery is stocked with: ", list(stocks))


if __name__ == '__main__':
    main()
