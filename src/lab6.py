"""
Основна програма для Лабораторної роботи № 6.
"""

import math
import requests

from card_game.deck import create_deck, shuffle_deck
from card_game.dealing import deal_cards


def main():
    """Основна функція для демонстрації використання модулів та пакетів."""
    print("=== ДЕМОНСТРАЦІЯ СТАНДАРТНОГО МОДУЛЯ СТОРОННЬОГО ПАКЕТА ===")
    
    # 1. Модуль стандартної бібліотеки (math)
    print(f"Квадратний корінь з 16: {math.sqrt(16)}")

    # 2. Сторонній пакет (requests)
    try:
        response = requests.get("https://api.github.com", timeout=10)
        response.raise_for_status()
        print("Успішно підключено до GitHub API.")
    except requests.exceptions.RequestException as e:
        print(f"Не вдалося підключитися до GitHub API: {e}")

    print("\n=== ДЕМОНСТРАЦІЯ ВЛАСНОГО ПАКЕТА CARD_GAME ===")
    
    # 3. Власний пакет (card_game)
    deck = create_deck()
    print(f"1. Створено колоду з {len(deck)} карт.")

    shuffled_deck = shuffle_deck(deck)
    print("2. Колоду успішно перемішано.")

    hands = deal_cards(shuffled_deck, players_count=3, cards_per_player=5)
    print("\n3. Результати роздачі карт (3 гравці по 5 карт):")
    for player, cards in hands.items():
        print(f"   {player}: {', '.join(cards)}")

    print(f"\nЗалишок карт у колоді: {len(shuffled_deck)}")


if __name__ == "__main__":
    main()