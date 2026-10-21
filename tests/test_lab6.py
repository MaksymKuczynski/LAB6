"""
Юніт-тести для Лабораторної роботи № 6.

Містить тести для перевірки функціональності пакета card_game.
"""
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from card_game.deck import create_deck, shuffle_deck # type: ignore
from card_game.dealing import deal_cards # type: ignore


class TestLab6(unittest.TestCase):

    def test_example(self):
        """Приклад тестового випадку."""
        self.assertEqual(2 + 2, 4)

    def test_create_deck(self):
        """Тестовий випадок для функції create_deck."""
        deck = create_deck()
        self.assertEqual(len(deck), 52)
        self.assertIn('A♠', deck)

    def test_shuffle_deck(self):
        """Тестовий випадок для функції shuffle_deck."""
        deck = create_deck()
        shuffled = shuffle_deck(deck)
        self.assertEqual(len(shuffled), 52)

    def test_deal_cards(self):
        """Тестовий випадок для функції deal_cards."""
        deck = create_deck()
        hands = deal_cards(deck, players_count=2, cards_per_player=5)
        self.assertEqual(len(hands), 2)
        self.assertEqual(len(hands["Гравець 1"]), 5)
        self.assertEqual(len(deck), 42)  # 52 - 10 = 42

    def test_deal_cards_edge_cases(self):
        """Тестовий випадок для deal_cards з граничними випадками та помилками."""
        deck = create_deck()
        # Спроба роздати більше карт, ніж є в колоді (ValueError)
        with self.assertRaises(ValueError):
            deal_cards(deck, players_count=10, cards_per_player=10)


if __name__ == '__main__':
    unittest.main()