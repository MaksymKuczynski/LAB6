"""Модуль deck для створення та перемішування колоди карт."""

import random

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def create_deck() -> list[str]:
    """Створює стандартну колоду з 52 карт."""
    return [f"{rank}{suit}" for suit in SUITS for rank in RANKS]


def shuffle_deck(deck: list[str]) -> list[str]:
    """Повертає перемішану копію колоди карт."""
    deck_copy = deck.copy()
    random.shuffle(deck_copy)
    return deck_copy