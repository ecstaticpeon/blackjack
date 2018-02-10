from random import shuffle

from .player import Player
from .utils import generate_deck


class Game:

    def __init__(self, cards):
        self.card_pool = cards
        self.shuffle_deck()

        self.player = Player()
        self.dealer = Player()

    @classmethod
    def create_game(cls):
        """
        Helper to start a game with a deck of card.
        """
        return cls(cards=generate_deck())

    def shuffle_deck(self):
        shuffle(self.card_pool)

    def deal(self, player):
        # TODO: handle empty deck.
        card = self.card_pool.pop(0)
        player.add_card(card)

    def start(self):
        self.deal(self.player)
        self.deal(self.player)
        self.deal(self.dealer)

    def complete_dealers_hand(self):
        hand = self.dealer.hand
        while hand.get_score() < 17 or (hand.is_soft and hand.get_score() == 17):
            self.deal(self.dealer)
