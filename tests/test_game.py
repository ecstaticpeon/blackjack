from unittest import TestCase
from unittest.mock import patch

from blackjack.card import Card, SUIT_SPADES
from blackjack.game import Game
from blackjack.player import Player


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

    def test_deal_card(self):
        dealt_card = Card(1, SUIT_SPADES)
        card_in_deck = Card(13, SUIT_SPADES)

        with patch.object(Game, 'shuffle_deck', autospec=True):
            game = Game([dealt_card, card_in_deck])
        player = Player()

        game.deal(player)

        self.assertEqual([card_in_deck], game.get_card_pool())
        self.assertEqual([dealt_card], player.get_hand().get_cards())

    def test_start_game(self):
        game = Game.create_game()
        game.start()
        player = game.get_player()
        dealer = game.get_dealer()
        self.assertEqual(2, len(player.get_hand().get_cards()), 'The player should be dealt 2 cards')
        self.assertEqual(1, len(dealer.get_hand().get_cards()), 'The dealer should be dealt 1 card')

    def test_complete_dealers_hand(self):
        # Cards given to the player.
        players_cards = [
            Card(1, SUIT_SPADES),
            Card(2, SUIT_SPADES),
        ]
        # Cards given to the dealer.
        dealers_cards = [
            Card(3, SUIT_SPADES),
            Card(7, SUIT_SPADES),
            Card(8, SUIT_SPADES),
        ]

        deck = players_cards + dealers_cards + [
            Card(9, SUIT_SPADES),
        ]
        with patch.object(Game, 'shuffle_deck', autospec=True):
            game = Game(deck)
            game.start()
            game.complete_dealers_hand()
            dealer = game.get_dealer()
            self.assertEqual(dealers_cards, dealer.get_hand().get_cards())

    def test_complete_dealers_hand_hits_on_soft_17(self):
        # Cards given to the player.
        players_cards = [
            Card(4, SUIT_SPADES),
            Card(5, SUIT_SPADES),
        ]
        # Cards given to the dealer.
        dealers_cards = [
            Card(1, SUIT_SPADES),
            Card(6, SUIT_SPADES),
            Card(2, SUIT_SPADES),
        ]

        deck = players_cards + dealers_cards + [
            Card(9, SUIT_SPADES),
        ]
        with patch.object(Game, 'shuffle_deck', autospec=True):
            game = Game(deck)
            game.start()
            game.complete_dealers_hand()
            dealer = game.get_dealer()
            self.assertEqual(dealers_cards, dealer.get_hand().get_cards(), 'Dealer must hit on a soft 17')

    def test_complete_dealers_hand_does_not_hit_on_hard_17(self):
        # Cards given to the player.
        players_cards = [
            Card(4, SUIT_SPADES),
            Card(5, SUIT_SPADES),
        ]
        # Cards given to the dealer.
        dealers_cards = [
            Card(10, SUIT_SPADES),
            Card(6, SUIT_SPADES),
            Card(1, SUIT_SPADES),
        ]

        deck = players_cards + dealers_cards + [
            Card(9, SUIT_SPADES),
        ]
        with patch.object(Game, 'shuffle_deck', autospec=True):
            game = Game(deck)
            game.start()
            game.complete_dealers_hand()
            dealer = game.get_dealer()
            self.assertEqual(dealers_cards, dealer.get_hand().get_cards(), 'Dealer must not hit on a hard 17')
