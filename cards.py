from random import shuffle
from itertools import product
from const import SUITS, RANKS


class Card:
    def __init__(self, suit, rank, points):
        self.suit = suit
        self.rank = rank
        self.point = points

    def __str__(self):
        return f'{self.suit}, {self.rank}'


class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
        shuffle(self.cards)

    @staticmethod
    def generate_deck():
        cards = []
        for suit, rank in product(SUITS, RANKS):
            points = 0
            if rank == 'Ace':
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10
            # picture = PRINTED.get(suit)
            c = Card(suit=suit, rank=rank, points=points)
            cards.append(c)
        return cards

    def get_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
