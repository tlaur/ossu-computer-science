from numb3rs import validate

def test_valid_addresses():
    assert validate("127.0.0.1") == True
    assert validate("10.1.2.34") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_part_num_too_big():
    assert validate("256.255.255.255") == False
    assert validate("255.256.255.255") == False
    assert validate("255.255.256.255") == False
    assert validate("255.255.255.256") == False

def test_part_num_too_small():
    assert validate("-1.0.0.0") == False
    assert validate("0.-1.0.0") == False
    assert validate("0.0.-1.0") == False
    assert validate("0.0.0.-1") == False

def test_part_non_numeric():
    assert validate("X.0.0.0") == False
    assert validate("0.O.0.0") == False
    assert validate("0.0...0") == False
    assert validate("0.0.0.?") == False

def test_parts_blank():
    assert validate("....") == False

def test_too_many_parts():
    assert validate("1.2.3.5.6") == False

def test_too_few_parts():
    assert validate("1.2.3") == False
    assert validate("1.2.") == False
    assert validate("1.2") == False
    assert validate("1") == False