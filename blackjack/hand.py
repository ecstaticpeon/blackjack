class Hand:

    def __init__(self):
        self.cards = []
        # A hand is soft if it has an ace which value is counted at 11 and could be reduced to 1.
        self.is_soft = False

    def add_card(self, card):
        self.cards.append(card)

    def get_cards(self):
        return self.cards

    def get_score(self):
        score = 0
        number_of_soft_aces = 0

        for card in self.cards:
            if card.rank > 10:
                # Faces count as 10.
                value = 10
            elif card.rank == 1:
                # Aces count as 11, or 1 if score > 21. Adjust later below.
                value = 11
                number_of_soft_aces += 1
                self.is_soft = True
            else:
                value = card.rank
            score += value

        # Adjust score if we've gone over 21 and we have aces.
        while score > 21 and number_of_soft_aces > 0:
            score -= 10
            number_of_soft_aces -= 1
            if number_of_soft_aces == 0:
                self.is_soft = False

        return score
