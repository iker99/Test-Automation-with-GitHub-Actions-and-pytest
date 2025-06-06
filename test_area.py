# archivo: test_suma.py
def area(b, h):
    if b <= 0 or h <= 0:
        return False
    else:
        return (b * h) / 2

def test_area_correcto():
    assert area(5, 7) == 17.5

def test_numeros_negativos():
    assert area(-3, 4) == False
    assert area(3, -4) == False

def test_base_no_cero():
    assert area(0, 2) == False