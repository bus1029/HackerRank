from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # __repr__은 시스템(Python Interpreter)이 해당 객체를 인식할 수 있는
    # 공식적인 문자열로 나타내줄 때 사용하는 것이다.
    def __repr__(self):
        pass

    def comparator(self, a, b):
        # Descending
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        elif a.score == b.score:

            # Ascending
            if a.name > b.name:
                return 1
            elif a.name == b.name:
                return 0
            else:
                return -1


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)