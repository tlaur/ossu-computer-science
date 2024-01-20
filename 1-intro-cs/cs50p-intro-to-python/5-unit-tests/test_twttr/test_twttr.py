from twttr import shorten

def test_remove_vowels():
    assert shorten("aeiou") == ""
    assert shorten("twitter") == "twttr"

def test_keep_consonants():
    assert shorten("qwrtypsdfghjklzxcvbnm") == "qwrtypsdfghjklzxcvbnm"

def test_case_unchanged():
    assert shorten("qqq") == "qqq"
    assert shorten("QQQ") == "QQQ"
    assert shorten("qQq") == "qQq"

def test_multiple_words():
    assert shorten("this is a test") == "ths s  tst"

def test_numbers():
    assert shorten("123") == "123"
    assert shorten("1 2 3") == "1 2 3"