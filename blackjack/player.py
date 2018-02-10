from .hand import Hand


class Player:

    def __init__(self):
        self.hand = Hand()

    def add_card(self, card):
        self.hand.add_card(card)
