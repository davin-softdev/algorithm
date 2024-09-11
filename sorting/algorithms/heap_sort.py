from strategy import SortingStrategy
from tqdm import tqdm  # Import tqdm for progress bar

class HeapSorting(SortingStrategy):
    def __init__(self):
        self.steps = 0

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        self.steps += 1

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def sort(self, data):
        self.steps = 0
        n = len(data)

        # Add a progress bar for the outer loop
        with tqdm(total=n, desc="Sorting Progress", unit="iteration") as pbar:
            for i in range(n // 2 - 1, -1, -1):
                self.heapify(data, n, i)

            for i in range(n - 1, 0, -1):
                self.steps += 1
                data[i], data[0] = data[0], data[i]
                self.heapify(data, i, 0)

                # Update progress bar
                pbar.update(1)

        return data
    