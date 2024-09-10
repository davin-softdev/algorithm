from strategy import SortingStrategy
from tqdm import tqdm  # Import tqdm for progress bar


class SelectionSorting(SortingStrategy):
    def __init__(self):
        self.steps = 0

    def sort(self, data):
        self.steps = 0
        # Implementing Selection Sort with tqdm progress bar
        n = len(data)
        # Add a progress bar for the outer loop
        for i in tqdm(range(n), desc="Sorting Progress", unit="iteration"):
            min_idx = i
            for j in range(i + 1, n):
                self.steps += 1  # Count the comparison
                if data[j] < data[min_idx]:
                    self.steps += 1  # Count the swap operation
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
        return data