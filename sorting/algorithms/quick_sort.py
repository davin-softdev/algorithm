from strategy import SortingStrategy
from tqdm import tqdm  # Import tqdm for progress bar

class QuickSorting(SortingStrategy):
    def __init__(self):
        self.steps = 0

    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            self.steps += 1
            if array[j] <= pivot:
                i += 1
                self.steps += 1
                array[i], array[j] = array[j], array[i]

        self.steps += 1
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quickSort(self, data, low, high, pbar):
        if low < high:
            pi = self.partition(data, low, high)

            # Update the progress bar after each partitioning
            pbar.update(1)

            self.quickSort(data, low, pi - 1, pbar)
            self.quickSort(data, pi + 1, high, pbar)

    def sort(self, data):
        self.steps = 0
        n = len(data)

        with tqdm(total=n, desc="Sorting Progress", unit="partition") as pbar:
            self.quickSort(data, 0, n - 1, pbar)

        return data
