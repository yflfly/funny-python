# coding:utf-8
import collections
from random import choice

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

# 从一叠牌中抽取特定的一张纸牌，比如说第一张或最后一张，这里是调用了 __getitem__ 方法提供的
print(deck[0])
print(deck[-1])
'''
# 输出结果
card(rank='2', suit='spades')
card(rank='A', suit='hearts')
'''

print(choice(deck))
print(choice(deck))
print(choice(deck))
'''
python内置了从一个序列中随机选出一个元素的函数random.choice，直接把它用在这一摞纸牌实例上就好
# 输出结果：
card(rank='Q', suit='hearts')
card(rank='2', suit='hearts')
card(rank='10', suit='hearts')
'''
