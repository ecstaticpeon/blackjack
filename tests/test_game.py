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
            self.assertCountEqual(expected_card_pool, game.get_card_pool())

    def test_card_pool_is_shuffled(self):
        with patch('blackjack.game.shuffle', autospec=True) as mock_shuffle:
            card_pool = [
                Card(1, SUIT_SPADES),
                Card(2, SUIT_SPADES),
            ]
            Game(card_pool)
            mock_shuffle.assert_called_once_with(card_pool)
