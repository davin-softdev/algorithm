import time
from algorithms.merge_sort import MergeSorting
from algorithms.heap_sort import HeapSorting
from algorithms.quick_sort import QuickSorting
from algorithms.shaker_sort import ShakerSorting
from algorithms.comb_sort import CombSorting
from algorithms.shell_sort import ShellSorting
from algorithms.bubble_sort import BubbleSorting
from algorithms.binary_insertion_sort import BinaryInsertionSorting
from algorithms.insertion_sort import InsertionSorting
from algorithms.double_selection_sort import DoubleSelectionSorting
from algorithms.selection_sort import SelectionSorting
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

def display_sorted_data_by_algorithms(name, algorithm, sorted_data):
    ## Run the algorithm and measure time
    sorted_data, elapsed_time, steps = measure_time(algorithm(), sorted_data)
    ## Print the result with the class name, then we can know which algorithm is being used
    print(f"{name}: -> {elapsed_time}")

    print(f"Steps: {steps}")
    return sorted_data

def main():
    data = generate_random_array(size=30000)

    # normal_sorted = display_sorted_data_by_algorithms("normal sorting",NormalSorting, data.copy())
    # selection_sorted = display_sorted_data_by_algorithms("selection sorting",SelectionSorting, data.copy())
    # double_selection_sorted =display_sorted_data_by_algorithms("double selection sorting",DoubleSelectionSorting, data.copy())
    # insertion_sorted = display_sorted_data_by_algorithms("insertion sorting",InsertionSorting, data.copy())
    binary_insertion_sorted = display_sorted_data_by_algorithms("binary insertion sorting",BinaryInsertionSorting, data.copy())
    # bubble_sorted = display_sorted_data_by_algorithms("bubble sorting",BubbleSorting, data.copy())
    # shaker_sorted = display_sorted_data_by_algorithms("shaker sorting",ShakerSorting, data.copy())
    quick_sorted = display_sorted_data_by_algorithms("quick sorting",QuickSorting, data.copy())
    merge_sort_sorted = display_sorted_data_by_algorithms("merge sorting",MergeSorting, data.copy())
    heap_sort_sorted = display_sorted_data_by_algorithms("heap sorting",HeapSorting, data.copy())
    comb_sorted = display_sorted_data_by_algorithms("comb sorting",CombSorting, data.copy())
    shell_sorted = display_sorted_data_by_algorithms("Shell sorting", ShellSorting, data.copy())

    # print(binary_insertion_sorted == normal_sorted == selection_sorted == double_selection_sorted == insertion_sorted)
    print(binary_insertion_sorted == quick_sorted == shell_sorted == merge_sort_sorted == heap_sort_sorted == comb_sorted)
    # print(bubble_sorted)

if __name__ == "__main__":
    main()
