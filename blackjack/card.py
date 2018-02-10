from collections import namedtuple

SUIT_HEARTS = 'hearts'
SUIT_DIAMONDS = 'diamonds'
SUIT_CLUBS = 'clubs'
SUIT_SPADES = 'spades'


class Card(namedtuple('Card', ['rank', 'suit'])):
    __slots__ = ()

    def __repr__(self):
        if self.rank == 1:
            rank = 'ace'
        elif self.rank == 11:
            rank = 'jack'
        elif self.rank == 12:
            rank = 'queen'
        elif self.rank == 13:
            rank = 'king'
        else:
            rank = self.rank

        return f'{rank} of {self.suit}'
