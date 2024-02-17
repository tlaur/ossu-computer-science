from um import count

def test_basic():
    assert count("um") == 1
    assert count("um um") == 2

def test_case_insensitive():
    assert count("Um uM UM") == 3

def test_valid_punctuation():
    assert count("um?") == 1
    assert count("um, um!") == 2
    assert count("um:") == 1
    assert count("um;") == 1
    assert count("um") == 1

def test_invalid():
    assert count("umm ummu") == 0
    assert count("um1") == 0
    assert count("um_") == 0
    assert count("um]") == 0
    assert count("[um") == 0
    assert count("um-") == 0
    assert count("um,um") == 1