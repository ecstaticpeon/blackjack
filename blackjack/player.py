from blackjack.hand import Hand


class Player:

    def __init__(self):
        self.hand = Hand()

    def get_hand(self):
        return self.hand

    def add_card(self, card):
        self.hand.add_card(card)
