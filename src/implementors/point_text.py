from src.core import Points

class Text_points(Points):
     def save(self):
         with open('points_text.txt', 'w', encoding='UTF-8') as f:
             for name in self.players:
                 f.write(f'{name}---{self.players.get(name)}\n')
     def load(self):
         with open('points_text.txt', 'r', encoding='UTF-8') as f:
             text = f.read()
             split_text = text.split('\n')
             split_text.remove('')
             for i in split_text:
                 now = i.split('---')
                 self.players[now[0]] = now[1]
                 print(self.players)