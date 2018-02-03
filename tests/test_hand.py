from unittest import TestCase

from blackjack.hand import Hand


class TestHand(TestCase):

    def test_score_is_sum_of_cards_for_non_faces_and_no_ace(self):
        hand = Hand([2, 3, 4])
        self.assertEqual(9, hand.get_score())

    def test_score_returns_ten_for_faces(self):
        hand = Hand([11, 12])
        self.assertEqual(20, hand.get_score())

    def test_score_with_aces(self):
        """
        Aces count as 11 if score is < 21.
        """
        hand = Hand([1])
        self.assertEqual(11, hand.get_score())

        # Score is just 21, the ace count as 11.
        hand = Hand([1, 10])
        self.assertEqual(21, hand.get_score())

        # 2 aces, one of them count as 11, the other as 1 to reduce the count from 22.
        hand = Hand([1, 1])
        self.assertEqual(12, hand.get_score())

        # 3 aces, 2 of them have to count as 1.
        hand = Hand([1, 1, 1])
        self.assertEqual(13, hand.get_score())
