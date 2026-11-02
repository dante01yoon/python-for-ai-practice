def shipping(total: float) -> float:
    if total >= 50:
        return 0.0
    if total >= 25:
        return 4.99
    return 7.99
