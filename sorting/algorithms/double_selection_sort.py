from strategy import SortingStrategy
from tqdm import tqdm  # Import tqdm for progress bar

class DoubleSelectionSorting(SortingStrategy):
    def __init__(self):
        self.steps = 0

    def sort(self, data):
        self.steps = 0
        n = len(data)
        j = n - 1

        # Initialize tqdm progress bar
        with tqdm(total=n, desc="Sorting Progress", unit="iteration") as pbar:
            for i in range(n):
                if i >= j:
                    break

                min_idx = i
                max_idx = j

                # Inner loop to find min and max elements
                for k in range(i + 1, j + 1):
                    self.steps += 1  # Count the comparison
                    if data[k] < data[min_idx]:
                        min_idx = k
                    if data[k] > data[max_idx]:
                        max_idx = k

                # Swap the found minimum and maximum with the appropriate positions
                if min_idx != i:
                    self.steps += 1  # Count the swap operation
                    data[i], data[min_idx] = data[min_idx], data[i]
                if max_idx != j:
                    self.steps += 1  # Count the swap operation
                    data[j], data[max_idx] = data[max_idx], data[j]

                j -= 1

                # Update progress bar based on the number of sorted elements
                pbar.update(2)

        return data
