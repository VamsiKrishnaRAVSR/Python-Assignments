from calculator import calculate

def test_basic_arithmetic():
    assert calculate('100+20') == 120
    assert calculate('100-20') == 80
    assert calculate('100/20') == 5
    assert calculate('100*3') == 300

def test_parentheses():
    assert calculate("(1 + 2) * 3") == 9
    assert calculate("4 - (5 * 6)") == -26

def test_exponents():
    assert calculate("2 ** 3") == 8

def test_negative_numbers():
    assert calculate("-1 + 2") == 1
    assert calculate("3 - (-4)") == 7
