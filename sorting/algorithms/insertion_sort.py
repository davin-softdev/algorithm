from strategy import SortingStrategy
from tqdm import tqdm  # Import tqdm for progress bar

class InsertionSorting(SortingStrategy):
    def __init__(self):
        self.steps = 0

    def sort(self, data):
        self.steps = 0
        # Implementing Insertion Sort with tqdm progress bar
        n = len(data)
        # Add a progress bar for the outer loop
        with tqdm(range(n), desc="Sorting Progress", unit="iteration") as pbar:
            for i in range(1, n):
                key = data[i]
                j = i - 1
                while j >= 0 and key < data[j]:
                    self.steps += 1  # Count the comparison
                    data[j + 1] = data[j]
                    j -= 1
                self.steps += 1  # Count the swap operation
                data[j + 1] = key

                pbar.update(1)
            pbar.update(1)
        return data
    