from .utils import generate_deck


class Game:

    def __init__(self, cards):
        self.card_pool = cards

    @classmethod
    def create_game(cls):
        """
        Helper to start a game with a deck of card.
        """
        return cls(cards=generate_deck())

    def get_card_pool(self):
        return self.card_pool
