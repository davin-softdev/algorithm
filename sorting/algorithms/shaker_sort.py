from strategy import SortingStrategy
from tqdm import tqdm  # Import tqdm for progress bar

class ShakerSorting(SortingStrategy):
    def __init__(self):
        self.steps = 0

    def sort(self, data):
        n = len(data)
        swapped = True
        start = 0
        end = n-1
        with tqdm(range(n), desc="Sorting Progress", unit="iteration") as pbar:
            while (swapped==True):
                # reset the swapped flag on entering the loop,
                # because it might be true from a previous
                # iteration.
                swapped = False
        
                # loop from left to right same as the bubble
                # sort
                for i in range (start, end):
                    self.steps += 1
                    if (data[i] > data[i+1]) :
                        self.steps += 1
                        data[i], data[i+1]= data[i+1], data[i]
                        swapped=True
        
                # if nothing moved, then array is sorted.
                if (swapped==False):
                    break
        
                # otherwise, reset the swapped flag so that it
                # can be used in the next stage
                swapped = False
        
                # move the end point back by one, because
                # item at the end is in its rightful spot
                end = end-1
        
                # from right to left, doing the same
                # comparison as in the previous stage
                for i in range(end-1, start-1,-1):
                    self.steps += 1
                    if (data[i] > data[i+1]):
                        self.steps += 1
                        data[i], data[i+1] = data[i+1], data[i]
                        swapped = True
        
                # increase the starting point, because
                # the last stage would have moved the next
                # smallest number to its rightful spot.
                start = start+1
                pbar.update(1)
        return data