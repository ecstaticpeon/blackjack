from unittest import TestCase

from blackjack.card import Card, SUIT_CLUBS, SUIT_DIAMONDS, SUIT_HEARTS, SUIT_SPADES
from blackjack.utils import generate_deck


class TestDeck(TestCase):

    def test_deck_creation(self):
        expected_cards = [
            Card(1, SUIT_CLUBS),
            Card(2, SUIT_CLUBS),
            Card(3, SUIT_CLUBS),
            Card(4, SUIT_CLUBS),
            Card(5, SUIT_CLUBS),
            Card(6, SUIT_CLUBS),
            Card(7, SUIT_CLUBS),
            Card(8, SUIT_CLUBS),
            Card(9, SUIT_CLUBS),
            Card(10, SUIT_CLUBS),
            Card(11, SUIT_CLUBS),
            Card(12, SUIT_CLUBS),
            Card(13, SUIT_CLUBS),

            Card(1, SUIT_DIAMONDS),
            Card(2, SUIT_DIAMONDS),
            Card(3, SUIT_DIAMONDS),
            Card(4, SUIT_DIAMONDS),
            Card(5, SUIT_DIAMONDS),
            Card(6, SUIT_DIAMONDS),
            Card(7, SUIT_DIAMONDS),
            Card(8, SUIT_DIAMONDS),
            Card(9, SUIT_DIAMONDS),
            Card(10, SUIT_DIAMONDS),
            Card(11, SUIT_DIAMONDS),
            Card(12, SUIT_DIAMONDS),
            Card(13, SUIT_DIAMONDS),

            Card(1, SUIT_HEARTS),
            Card(2, SUIT_HEARTS),
            Card(3, SUIT_HEARTS),
            Card(4, SUIT_HEARTS),
            Card(5, SUIT_HEARTS),
            Card(6, SUIT_HEARTS),
            Card(7, SUIT_HEARTS),
            Card(8, SUIT_HEARTS),
            Card(9, SUIT_HEARTS),
            Card(10, SUIT_HEARTS),
            Card(11, SUIT_HEARTS),
            Card(12, SUIT_HEARTS),
            Card(13, SUIT_HEARTS),

            Card(1, SUIT_SPADES),
            Card(2, SUIT_SPADES),
            Card(3, SUIT_SPADES),
            Card(4, SUIT_SPADES),
            Card(5, SUIT_SPADES),
            Card(6, SUIT_SPADES),
            Card(7, SUIT_SPADES),
            Card(8, SUIT_SPADES),
            Card(9, SUIT_SPADES),
            Card(10, SUIT_SPADES),
            Card(11, SUIT_SPADES),
            Card(12, SUIT_SPADES),
            Card(13, SUIT_SPADES),
        ]

        self.assertCountEqual(expected_cards, generate_deck())
