import pytest
from kalkulator import dodaj
from kalkulator import dziel

# def test_dodawania_liczb_dodatnich():
#     assert dodaj(2,3) == 5
#
# def test_dodawania_liczb_ujemnych():
#     assert dodaj(-2,-3) == -5
#
# def test_dzielenia_przez_zero_powinno_rzucic_blad():
#     with pytest.raises(ZeroDivisionError):
#         dziel(5,0)
#
# def test_poprawnego_dzielenia():
#     assert dziel(5,5) == 1

@pytest.mark.parametrize("a,b,expected", [
    (3,3,6),
    (-2,-2,-4),
    (-2,3,1),
    (4,0,4)
])
def test_dodawania_wielu_przypadkow(a,b,expected):
    assert dodaj(a,b) == expected