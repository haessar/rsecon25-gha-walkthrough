from arithmetic.addition import sum_two_integers

def test_add():
    assert sum_two_integers(1, 2) == 3
    assert sum_two_integers(2, 2) != 5
