# coding:utf-8
import collections

# 构建了一个简单的类来白哦是一张纸牌
Card = collections.namedtuple('card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)  # 52

    def __getitem__(self, position):
        return self._cards[position]


# 使用 可以用len()函数来查看一叠牌有多少张
deck = FrenchDeck()
print(len(deck))
