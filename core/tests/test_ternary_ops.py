from core.ternary_ops import trinary_and, trinary_or, trinary_not

def test_trinary_and():
    assert trinary_and(1, 1) == 1
    assert trinary_and(0, 1) == 0
    assert trinary_and(-1, 1) == -1

def test_trinary_not():
    assert trinary_not(1) == -1
    assert trinary_not(0) == 0
    assert trinary_not(-1) == 1
