from unittest import TestCase

from blackjack.card import Card, SUIT_SPADES
from blackjack.hand import Hand


def create_hand(cards):
    hand = Hand()
    for card in cards:
        hand.add_card(card)
    return hand


class TestHand(TestCase):

    def test_score_is_sum_of_cards_for_non_faces_and_no_ace(self):
        hand = create_hand([
            Card(2, SUIT_SPADES),
            Card(3, SUIT_SPADES),
            Card(4, SUIT_SPADES),
        ])
        self.assertEqual(9, hand.get_score())

    def test_score_returns_ten_for_faces(self):
        hand = create_hand([
            Card(11, SUIT_SPADES),
            Card(12, SUIT_SPADES),
        ])
        self.assertEqual(20, hand.get_score())

    def test_score_with_aces(self):
        """
        Aces count as 11 if score is < 21.
        """
        hand = create_hand([
            Card(1, SUIT_SPADES),
        ])
        self.assertEqual(11, hand.get_score())

        # Score is just 21, the ace count as 11.
        hand = create_hand([
            Card(1, SUIT_SPADES),
            Card(10, SUIT_SPADES),
        ])
        self.assertEqual(21, hand.get_score())

        # 2 aces, one of them count as 11, the other as 1 to reduce the count from 22.
        hand = create_hand([
            Card(1, SUIT_SPADES),
            Card(1, SUIT_SPADES),
        ])
        self.assertEqual(12, hand.get_score())

        # 3 aces, 2 of them have to count as 1.
        hand = create_hand([
            Card(1, SUIT_SPADES),
            Card(1, SUIT_SPADES),
            Card(1, SUIT_SPADES),
        ])
        self.assertEqual(13, hand.get_score())
