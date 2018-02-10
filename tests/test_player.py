from unittest import TestCase

from blackjack.card import Card, SUIT_SPADES
from blackjack.player import Player


class TestPlayer(TestCase):

    def test_player_starts_empty_handed(self):
        player = Player()
        self.assertEqual([], player.hand.cards)

    def test_add_card(self):
        player = Player()
        ace_of_spades = Card(1, SUIT_SPADES)
        two_of_spades = Card(2, SUIT_SPADES)

        player.add_card(ace_of_spades)
        self.assertEqual(
            [ace_of_spades],
            player.hand.cards,
        )

        player.add_card(two_of_spades)
        self.assertEqual(
            [ace_of_spades, two_of_spades],
            player.hand.cards,
        )
