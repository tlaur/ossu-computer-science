from plates import is_valid

# It would be better to test the individual functions
# evaluated by is_valid(), but this will do for now.

def test_start_two_letters():
    assert is_valid("asdasd") == True
    assert is_valid("123asdasd") != True

def test_min_max_characters():
    assert is_valid("qw") == True
    assert is_valid("qwerty") == True
    assert is_valid("q") != True
    assert is_valid("qwertyu") != True

def test_no_nums_in_middle():
    assert is_valid("ab12cd") != True

def test_first_num_not_zero():
    assert is_valid("0abc") != True
    assert is_valid("572abc") != True

def test_only_alphanumeric():
    assert is_valid("ab!cd") != True
    assert is_valid("abcd?") != True
    assert is_valid("abc[d") != True
