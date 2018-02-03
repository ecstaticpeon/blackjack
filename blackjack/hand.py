class Hand:

    def __init__(self, cards):
        """
        :param cards: List of integers representing cards.
        """
        self.cards = cards

    def get_score(self):
        score = 0
        number_of_soft_aces = 0

        for card in self.cards:
            if card > 10:
                # Faces count as 10.
                value = 10
            elif card == 1:
                # Aces count as 11, or 1 if score > 21. Adjust later below.
                value = 11
                number_of_soft_aces += 1
            else:
                value = card
            score += value

        # Adjust score if we've gone over 21 and we have aces.
        while score > 21 and number_of_soft_aces > 0:
            score -= 10
            number_of_soft_aces -= 1

        return score
