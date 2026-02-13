"""Domain helpers for the Python validation fixture."""


def normalize_order_total(raw_total: float, tax_rate: float = 0.0) -> float:
    if raw_total < 0:
        raise ValueError("raw_total cannot be negative")
    total = raw_total * (1 + tax_rate)
    return round(total, 2)
