from app.service import normalize_order_total


def test_normalize_order_total_with_tax() -> None:
    assert normalize_order_total(100.0, 0.1) == 110.0
