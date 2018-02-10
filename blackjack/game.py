from random import shuffle

from .player import Player
from .utils import generate_deck


class Game:
    ACTION_HIT = 'hit'
    ACTION_STAND = 'stand'

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

    def get_available_actions(self):
        if self.player.hand.get_score() >= 21:
            return ()

        return (
            self.ACTION_HIT,
            self.ACTION_STAND,
        )

    def complete_dealers_hand(self):
        hand = self.dealer.hand
        while hand.get_score() < 17 or (hand.is_soft and hand.get_score() == 17):
            self.deal(self.dealer)

    def get_winner(self):
        dealer_score = self.dealer.hand.get_score()
        player_score = self.player.hand.get_score()

        if self.player.hand.is_bust():
            return self.dealer
        elif self.player.hand.is_blackjack():
            return self.player
        elif not self.dealer.hand.is_bust() and dealer_score > player_score:
            return self.dealer
        elif dealer_score == player_score:
            return None
        else:
            return self.player
