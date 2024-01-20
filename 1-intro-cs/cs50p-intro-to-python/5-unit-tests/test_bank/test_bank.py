from bank import value

def test_start_with_hello():
    assert value("hello") == 0
    assert value("hello there") == 0
    assert value("HELLO there") == 0
    assert value("hEllO tHerE sTraNger") == 0

def test_start_with_h():
    assert value("hey") == 20
    assert value("hey there") == 20
    assert value("HEY there") == 20
    assert value("hOla tHerE sTraNger") == 20

def test_start_with_other():
    assert value("") == 100
    assert value("    ") == 100
    assert value("Oh hi there") == 100
    assert value("What's up, how are you?") == 100