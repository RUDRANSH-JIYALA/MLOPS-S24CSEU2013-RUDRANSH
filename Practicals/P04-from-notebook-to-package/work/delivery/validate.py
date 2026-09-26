"Is this order usable?"


def is_valid_order(order):
    "True if the order passes every rule."

    if not isinstance(order, dict):
        return False

    try:
        distance = order["distance_km"]
        prep_time = order["prep_time_min"]
        traffic = order["traffic_level"]
        rain = order["rain"]
    except (KeyError, TypeError):
        return False

    if distance <= 0:
        return False

    if prep_time < 0:
        return False

    if traffic not in (1, 2, 3):
        return False

    if rain not in (0, 1):
        return False

    return True
