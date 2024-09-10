class SortContext:
    def __init__(self, strategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def sort_data(self, data):
        return self._strategy.sort(data)
