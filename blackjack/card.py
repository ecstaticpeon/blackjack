SUIT_HEARTS = 'hearts'
SUIT_DIAMONDS = 'diamonds'
SUIT_CLUBS = 'clubs'
SUIT_SPADES = 'spades'


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

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
