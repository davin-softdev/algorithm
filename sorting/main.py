import time
from context import SortContext
from algorithms.normal_sorting import NormalSorting
import random

### generate random number data
def generate_random_array(size=100, low=0, high=1000):
    ### generate random array
    ### size: size of array
    ### low: lower bound
    ### high: upper bound
    return [random.randint(low, high) for _ in range(size)]

### we need to measure time for each algorithm
### sort_strategy: Sorting strategy to be used
### data: data to be sorted
def measure_time(sort_strategy, data):
    ### measure time for each algorithm
    ### sort_strategy: Sorting strategy to be used
    ### data: data to be sorted

    ## First: get the sorting context -> will according to sort_strategy arg
    context = SortContext(sort_strategy)

    ## start counting
    start = time.time()

    ## Second: call sort method
    sorted_data = context.sort_data(data)

    ## end counting
    end = time.time()

    elapsed_time = end - start

    return sorted_data, elapsed_time, sort_strategy.steps

def main():
    data = generate_random_array(size=10000)

    sorted_data, elapsed_time, steps = measure_time(NormalSorting(), data.copy())

    print(f"NormalSorting: -> {elapsed_time}")

    print(f"Steps: {steps}")

if __name__ == "__main__":
    main()
