from abc import ABC, abstractmethod
class Points(ABC):
    def __init__(self):
        self.players = {}

    def add_players(self, name):
        self.players[name] = 0

    def plus_point(self, name):
        self.players[name] += 1

    def minus_point(self, name):
        self.players[name] -= 1

    @abstractmethod
    def save(self):
        ...

    @abstractmethod
    def load(self):
        ...
