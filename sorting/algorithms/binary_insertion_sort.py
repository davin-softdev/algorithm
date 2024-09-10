from strategy import SortingStrategy
from tqdm import tqdm  # Import tqdm for progress bar

class BinaryInsertionSorting(SortingStrategy):
    def __init__(self):
        self.steps = 0

    def binary_search(self, data, val, start, end):
        if start > end:
            return start
        
        mid = (start + end) // 2
        self.steps += 1  # Count comparison
        if data[mid] < val:
            return self.binary_search(data, val, mid + 1, end)
        else:
            return self.binary_search(data, val, start, mid - 1)

    def sort(self, data):
        self.steps = 0
        n = len(data)

        # Convert the data to a list to perform in-place modifications
        data = list(data)

        # Add a progress bar for the outer loop
        with tqdm(range(1, n), desc="Sorting Progress", unit="iteration") as pbar:
            for i in range(1, n):
                key = data[i]
                j = self.binary_search(data, key, 0, i - 1)

                # Insert the key into its correct position
                # This is the efficient in-place insertion
                data = data[:j] + [key] + data[j:i] + data[i + 1:]

                # Update progress bar
                pbar.update(1)

        return data
