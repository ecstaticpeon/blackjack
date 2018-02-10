from .game import Game
from .card import SUIT_CLUBS, SUIT_DIAMONDS, SUIT_HEARTS, SUIT_SPADES


class BlackjackCli:

    def play(self):
        print('\n♣♣♣ Hello. Let\'s play some Blackjack! ♣♣♣\n\n')

        game = Game.create_game()
        game.start()

        self.display_dealers_hand(game)

        actions = game.get_available_actions()

        while len(actions):
            self.display_players_hand(game)

            print('\nWhat do you say?\n')

            chosen_action = None
            while chosen_action is None:
                for index, action in enumerate(actions):
                    print(f'{index + 1}. {action}')

                user_input = input('\n> ')
                try:
                    chosen_action_index = int(user_input) - 1
                except ValueError:
                    print('\nPlease enter the number of your choice.\n')
                else:
                    try:
                        chosen_action = actions[chosen_action_index]
                    except IndexError:
                        print(f'\nPlease enter a choice between 1 and {len(actions)}.\n')

            print('')

            if chosen_action == game.ACTION_HIT:
                game.deal(game.player)
            elif chosen_action == game.ACTION_STAND:
                break

            actions = game.get_available_actions()

        game.complete_dealers_hand()

        print('\n')

        self.display_players_hand(game)
        if not game.player.hand.is_bust() and not game.player.hand.is_blackjack():
            self.display_dealers_hand(game)

        print('\n')

        winner = game.get_winner()
        if winner == game.player:
            print('Congratulations, you win!')
        elif winner == game.dealer:
            print('Oh no, the dealer won :(…')
        else:
            print('This is a draw!')

        print('')

    def display_players_hand(self, game):
        players_hand = game.player.hand
        print(f'You have {players_hand.get_score()} points.\n')
        print('|', ' | '.join([self.get_card_display(card) for card in players_hand.cards]), '|\n')

    def display_dealers_hand(self, game):
        dealers_hand = game.dealer.hand
        print(f'The dealer has {dealers_hand.get_score()} points.\n')
        print('|', ' | '.join([self.get_card_display(card) for card in dealers_hand.cards]), '|\n')

    @staticmethod
    def get_card_display(card):
        rank = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}.get(card.rank, str(card.rank))
        suit = {SUIT_CLUBS: '♣', SUIT_DIAMONDS: '♦', SUIT_HEARTS: '♥', SUIT_SPADES: '♠'}.get(card.suit)

        return f'{rank}{suit}'
