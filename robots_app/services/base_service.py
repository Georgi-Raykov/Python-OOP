from abc import ABC, abstractmethod


class BaseService(ABC):

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.robots = []

    @abstractmethod
    def details(self):
        pass
