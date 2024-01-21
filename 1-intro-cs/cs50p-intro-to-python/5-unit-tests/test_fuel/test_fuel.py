import pytest
from fuel import convert, gauge

def test_convert_valid_input():
    assert convert("20/100") == 20
    assert convert("0/1000") == 0
    assert convert("10000/10000") == 100
    assert convert("40/80") == 50

def test_convert_rounding():
    assert convert("255/1000") == 26
    assert convert("256/1000") == 26
    assert convert("254/1000") == 25

def test_convert_value_too_large():
    with pytest.raises(Exception):
        convert("101/100")

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("cat/cat")

def test_convert_exception():
    with pytest.raises(Exception):
        convert(10)

def test_gauge_partly_filled():
    assert gauge(2) == "2%"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(98) == "98%"

def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"