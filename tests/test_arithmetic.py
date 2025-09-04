from arithmetic.addition import sum_nested_ints

def test_sum_nested_ints():
    assert sum_nested_ints(1, 2) == 3
    assert sum_nested_ints(2, 2) != 5
    assert sum_nested_ints([1, 2], 3) == 6
