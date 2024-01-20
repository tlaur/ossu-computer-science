from hello import hello

def test_default():
    assert hello() == f"hello, world"

def test_argument():
    assert hello("David") == f"hello, David"

