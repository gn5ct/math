from src.core import Points

class Text_points(Points):
    def save(self):
        with open('points_text.txt')