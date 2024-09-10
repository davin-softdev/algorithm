from strategy import SortingStrategy
from tqdm import tqdm  # Import tqdm for progress bar
class NormalSorting(SortingStrategy):
    def __init__(self):
        self.steps = 0

    def sort(self, data):
        self.steps = 0
        # Implementing Bubble Sort with tqdm progress bar
        n = len(data)
        # Add a progress bar for the outer loop
        for i in tqdm(range(n), desc="Sorting Progress", unit="iteration"):
            for j in range(0, n-i-1):
                self.steps += 1  # Count the comparison
                if data[j] > data[j + 1]:
                    self.steps += 1  # Count the swap operation
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data