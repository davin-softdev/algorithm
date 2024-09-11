from strategy import SortingStrategy
from tqdm import tqdm  # Import tqdm for progress bar

class BubbleSorting(SortingStrategy):
    def __init__(self) -> None:
        self.steps = 0

    def sort(self, data):
        with tqdm(range(len(data) - 1, 0, -1), desc="Sorting Progress", unit="iteration") as pbar:
            # Outer loop to iterate through the list n times
            for n in range(len(data) - 1, 0, -1):
                # Inner loop to compare adjacent elements
                for i in range(n):
                    self.steps += 1  # Count comparison
                    if data[i] > data[i + 1]:
                        self.steps += 1  # Count comparison
                        # Swap elements if they are in the wrong order
                        swapped = True
                        data[i], data[i + 1] = data[i + 1], data[i]
                
                # Update progress bar
                pbar.update(1)

        return data
