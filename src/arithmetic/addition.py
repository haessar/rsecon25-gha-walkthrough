from typing import Union, Iterable


def sum_nested_ints(*args: Union[int, Iterable]) -> int:
    output = 0
    for i in args:
        if isinstance(i, int):
            output += i
        elif isinstance(i, Iterable):
            output += sum_nested_ints(*i)
    return output


# def sum_ints(xs):
#     # This dtype name was removed in NumPy 1.24
#     arr = np.asarray(xs, dtype=np.int)  # AttributeError on >=1.24
#     return int(arr.sum())
