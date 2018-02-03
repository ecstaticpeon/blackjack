from unittest import TestCase

from blackjack.card import Card, SUIT_SPADES, SUIT_HEARTS


class TestCard(TestCase):

    def test_equality(self):
        self.assertEqual(
            Card(1, SUIT_SPADES),
            Card(1, SUIT_SPADES),
        )
        self.assertNotEqual(
            Card(1, SUIT_SPADES),
            Card(2, SUIT_SPADES),
        )
        self.assertNotEqual(
            Card(1, SUIT_SPADES),
            Card(1, SUIT_HEARTS),
        )

    def test_hash(self):
        ace_of_spades = Card(1, SUIT_SPADES)
        ace_of_spades_2 = Card(1, SUIT_SPADES)
        ace_of_hearts = Card(1, SUIT_HEARTS)
        king_of_spades = Card(13, SUIT_SPADES)

        self.assertEqual(
            ace_of_spades.__hash__(),
            ace_of_spades_2.__hash__(),
            f'The {ace_of_spades} should share the same hash across all instances',
        )
        self.assertNotEqual(
            ace_of_spades.__hash__(),
            ace_of_hearts.__hash__(),
            f'The {ace_of_spades} and the {ace_of_hearts} should not share the same hash',
        )
        self.assertNotEqual(
            ace_of_spades.__hash__(),
            king_of_spades.__hash__(),
            f'The {ace_of_spades} and the {king_of_spades} should not share the same hash',
        )
