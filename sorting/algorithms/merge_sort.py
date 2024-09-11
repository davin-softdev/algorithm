from strategy import SortingStrategy
from tqdm import tqdm  # Import tqdm for progress bar

class MergeSorting(SortingStrategy):
    def __init__(self):
        self.steps = 0

    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2
        for i in range(0, n1):
            self.steps += 1
            L[i] = arr[l + i]
        for j in range(0, n2):
            self.steps += 1
            R[j] = arr[m + 1 + j]

        i, j = 0, 0
        k = l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                self.steps += 1
                arr[k] = L[i]
                i += 1
            else:
                self.steps += 1
                arr[k] = R[j]
                j += 1  

            self.steps += 1
            k += 1

        while i < n1:
            self.steps += 1
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < n2:
            self.steps += 1
            arr[k] = R[j]
            j += 1
            k += 1
        
    def mergeSort(self, arr, l, r, pbar):
        if l < r:
            m = (l + (r - l) // 2)
            self.mergeSort(arr, l, m, pbar)
            self.mergeSort(arr, m + 1, r, pbar)
            self.merge(arr, l, m, r)

            # Update the progress bar after each merge operation
            pbar.update(1)

    def sort(self, data):
        self.steps = 0
        n = len(data)

        with tqdm(total=n, desc="Sorting Progress", unit="merge") as pbar:
            self.mergeSort(data, 0, n - 1, pbar)

        return data
