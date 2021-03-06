from .card import Card, SUIT_CLUBS, SUIT_DIAMONDS, SUIT_HEARTS, SUIT_SPADES


def generate_deck():
    cards = []
    for suit in (SUIT_CLUBS, SUIT_DIAMONDS, SUIT_HEARTS, SUIT_SPADES, ):
        for rank in range(1, 14):
            cards.append(Card(rank, suit))
    return cards
