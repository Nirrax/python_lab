import pytest
from ad_4 import Prostokat


def test_inicjalizacja_poprawna():
    p = Prostokat(4, 5)
    assert p.szerokosc == 4
    assert p.wysokosc == 5


def test_inicjalizacja_bledne_dane():
    with pytest.raises(ValueError):
        Prostokat(-3, 5)

    with pytest.raises(ValueError):
        Prostokat(3, 0)


def test_pole():
    p = Prostokat(3, 7)
    assert p.pole() == 21


def test_obwod():
    p = Prostokat(4, 6)
    assert p.obwod() == 20
