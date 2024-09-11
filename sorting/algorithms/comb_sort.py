from strategy import SortingStrategy
from tqdm import tqdm  # Import tqdm for progress bar

class CombSorting(SortingStrategy):
    def __init__(self):
        self.steps = 0
    
    def getNextGap(self, gap):
        gap = (gap * 10) // 13
        if gap < 1:
            return 1
        return gap
    
    def combSort(self, data, pbar):
        self.steps = 0
        n = len(data)
 
        # Initialize gap
        gap = n
    
        # Initialize swapped as true to make sure that
        # loop runs
        swapped = True
    
        # Keep running while gap is more than 1 and last
        # iteration caused a swap
        while gap != 1 or swapped == 1:
    
            # Find next gap
            gap = self.getNextGap(gap)
    
            # Initialize swapped as false so that we can
            # check if swap happened or not
            swapped = False
    
            # Compare all elements with current gap
            for i in range(0, n-gap):
                
                if data[i] > data[i + gap]:
                    data[i], data[i + gap] = data[i + gap], data[i]
                    swapped = True

                    self.steps += 1
                    pbar.update(1)
            self.steps += 1


    def sort(self, data):
        self.steps = 0
        n = len(data)

        with tqdm(total=n, desc="Sorting Progress", unit="iteration") as pbar:
            self.combSort(data, pbar)

        return data
    