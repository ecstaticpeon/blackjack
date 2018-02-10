#!/usr/bin/env python3

from blackjack.cli import BlackjackCli

try:
    BlackjackCli().play()
except KeyboardInterrupt:
    print('\n\nBye!')
