"""Модуль dealing для роздачі карт гравцям."""


def deal_cards(deck: list[str], players_count: int, cards_per_player: int) -> dict[str, list[str]]:
    """Роздає задану кількість карт гравцям."""
    if players_count * cards_per_player > len(deck):
        raise ValueError("У колоді недостатньо карт для такої роздачі!")

    hands = {}
    for i in range(1, players_count + 1):
        hands[f"Гравець {i}"] = [deck.pop(0) for _ in range(cards_per_player)]

    return hands