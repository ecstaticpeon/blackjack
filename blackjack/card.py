from collections import namedtuple

SUIT_HEARTS = 'hearts'
SUIT_DIAMONDS = 'diamonds'
SUIT_CLUBS = 'clubs'
SUIT_SPADES = 'spades'


class Card(namedtuple('Card', ['value', 'suit'])):

    def __repr__(self):
        if self.value == 1:
            value = 'ace'
        elif self.value == 11:
            value = 'jack'
        elif self.value == 12:
            value = 'queen'
        elif self.value == 13:
            value = 'king'
        else:
            value = self.value

        return f'{value} of {self.suit}'

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def __hash__(self):
        if self.suit == SUIT_CLUBS:
            suit_value = 100
        elif self.suit == SUIT_DIAMONDS:
            suit_value = 200
        elif self.suit == SUIT_HEARTS:
            suit_value = 300
        elif self.suit == SUIT_SPADES:
            suit_value = 400
        else:
            raise ValueError(f'Cannot create hash for unknown suit "{self.suit}"')

        return self.value + suit_value
