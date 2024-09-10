from strategy import SortingStrategy

class NormalSorting(SortingStrategy):
    def sort(self, data):
        data = list(data)
        data.sort()
        return data