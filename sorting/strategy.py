from abc import ABC, abstractmethod

## Strategy
## - Strategy design pattern
## - Define a family of algorithms, encapsulate each one, and make them interchangeable.

## ABC: Abstract Base Class

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass
