from random import shuffle

from .utils import generate_deck


class Game:

    def __init__(self, cards):
        self.card_pool = cards
        self.shuffle_deck()

    @classmethod
    def create_game(cls):
        """
        Helper to start a game with a deck of card.
        """
        return cls(cards=generate_deck())

    def get_card_pool(self):
        return self.card_pool

    def shuffle_deck(self):
        shuffle(self.card_pool)

    def deal(self, player):
        # TODO: handle empty deck.
        card = self.card_pool.pop(0)
        player.add_card(card)
