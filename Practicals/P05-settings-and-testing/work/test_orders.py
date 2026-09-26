from delivery.validate import is_valid_order


def test_valid_order():
    order = {"distance_km": 10, "prep_time_min": 25, "traffic_level": 3, "rain": 0}
    assert is_valid_order(order) is True


def test_invalid_distance():
    order = {"distance_km": 0, "prep_time_min": 25, "traffic_level": 3, "rain": 0}
    assert is_valid_order(order) is False


def test_invalid_traffic():
    order = {"distance_km": 10, "prep_time_min": 25, "traffic_level": 4, "rain": 0}
    assert is_valid_order(order) is False
