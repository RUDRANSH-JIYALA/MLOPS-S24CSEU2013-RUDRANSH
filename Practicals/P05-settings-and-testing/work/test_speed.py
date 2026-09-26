from delivery.features import average_speed_kmph


def test_average_speed_basic():
    assert average_speed_kmph(10, 30) == 20


def test_average_speed_another_case():
    assert average_speed_kmph(20, 60) == 20
