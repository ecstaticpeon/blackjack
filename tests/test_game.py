from unittest import TestCase
from unittest.mock import patch

from blackjack.card import Card, SUIT_SPADES
from blackjack.game import Game


class TestGame(TestCase):

    def test_card_pool_creation(self):
        expected_card_pool = [
            Card(1, SUIT_SPADES),
            Card(2, SUIT_SPADES),
        ]
        with patch('blackjack.game.generate_deck', autospec=True, return_value=expected_card_pool):
            game = Game.create_game()
            self.assertEqual(expected_card_pool, game.get_card_pool())
