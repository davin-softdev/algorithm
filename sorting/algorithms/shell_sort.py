from strategy import SortingStrategy
from tqdm import tqdm  # Import tqdm for progress bar

class ShellSorting(SortingStrategy):
    def __init__(self):
        self.steps = 0

    def sort(self, data):
        self.steps = 0
        n = len(data)
        gap = n // 2
        with tqdm(total=n, desc="Sorting Progress", unit="iteration") as pbar:
            while gap > 0:
                for i in range(gap, n):
                    temp = data[i]
                    j = i
                    while j >= gap and data[j - gap] > temp:
                        self.steps += 1
                        data[j] = data[j - gap]
                        j -= gap
                    data[j] = temp
                gap //= 2
        return data
    