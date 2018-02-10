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
            self.assertCountEqual(expected_card_pool, game.card_pool)

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

        self.assertEqual([card_in_deck], game.card_pool)
        self.assertEqual([dealt_card], player.hand.cards)

    def test_start_game(self):
        game = Game.create_game()
        game.start()
        player = game.player
        dealer = game.dealer
        self.assertEqual(2, len(player.hand.cards), 'The player should be dealt 2 cards')
        self.assertEqual(1, len(dealer.hand.cards), 'The dealer should be dealt 1 card')

    def test_available_actions_during_play(self):
        game = Game([])

        self.assertEqual(
            (game.ACTION_HIT, game.ACTION_STAND, ),
            game.get_available_actions()
        )

    def test_available_actions_at_end_of_game(self):
        # Player has won.
        game = Game([])

        game.player.add_card(Card(1, SUIT_SPADES))
        game.player.add_card(Card(13, SUIT_SPADES))

        self.assertEqual(
            (),
            game.get_available_actions()
        )

        # Player has gone bust.
        game = Game([])

        game.player.add_card(Card(10, SUIT_SPADES))
        game.player.add_card(Card(10, SUIT_SPADES))
        game.player.add_card(Card(10, SUIT_SPADES))

        self.assertEqual(
            (),
            game.get_available_actions()
        )

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
            dealer = game.dealer
            self.assertEqual(dealers_cards, dealer.hand.cards)

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
            dealer = game.dealer
            self.assertEqual(dealers_cards, dealer.hand.cards, 'Dealer must hit on a soft 17')

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
            dealer = game.dealer
            self.assertEqual(dealers_cards, dealer.hand.cards, 'Dealer must not hit on a hard 17')

    def test_winner_has_highest_score(self):
        game = Game([])
        game.player.add_card(Card(10, SUIT_SPADES))
        game.dealer.add_card(Card(5, SUIT_SPADES))
        self.assertEqual(game.player, game.get_winner())

        game = Game([])
        game.player.add_card(Card(5, SUIT_SPADES))
        game.dealer.add_card(Card(10, SUIT_SPADES))
        self.assertEqual(game.dealer, game.get_winner())

    def test_winner_for_draws(self):
        game = Game([])
        game.player.add_card(Card(10, SUIT_SPADES))
        game.dealer.add_card(Card(10, SUIT_SPADES))
        self.assertIsNone(game.get_winner())

    def test_bust_hand_cannot_win(self):
        # Dealer is bust.
        game = Game([])

        game.player.add_card(Card(5, SUIT_SPADES))

        game.dealer.add_card(Card(10, SUIT_SPADES))
        game.dealer.add_card(Card(10, SUIT_SPADES))
        game.dealer.add_card(Card(10, SUIT_SPADES))

        self.assertEqual(game.player, game.get_winner())

        # Player is bust: dealer automatically wins.
        game = Game([])

        game.player.add_card(Card(10, SUIT_SPADES))
        game.player.add_card(Card(10, SUIT_SPADES))
        game.player.add_card(Card(10, SUIT_SPADES))

        game.dealer.add_card(Card(10, SUIT_SPADES))
        game.dealer.add_card(Card(10, SUIT_SPADES))
        game.dealer.add_card(Card(10, SUIT_SPADES))

        self.assertEqual(game.dealer, game.get_winner())

    def test_blackjack_always_wins(self):
        # If a player has a blackjack (e.g. their two first cards total
        # 21 points) they automatically win.
        game = Game([])

        game.player.add_card(Card(1, SUIT_SPADES))
        game.player.add_card(Card(13, SUIT_SPADES))

        game.dealer.add_card(Card(1, SUIT_SPADES))
        game.dealer.add_card(Card(13, SUIT_SPADES))

        self.assertEqual(game.player, game.get_winner())

        # Player may have 21 points without having a blackjack.
        game = Game([])

        game.player.add_card(Card(9, SUIT_SPADES))
        game.player.add_card(Card(10, SUIT_SPADES))
        game.player.add_card(Card(2, SUIT_SPADES))

        game.dealer.add_card(Card(1, SUIT_SPADES))
        game.dealer.add_card(Card(13, SUIT_SPADES))

        self.assertIsNone(game.get_winner(), 'Game should be a draw')
