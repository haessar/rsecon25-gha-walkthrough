from typing import Union, Iterable

def sum_nested_ints(*args: Union[Iterable, int]) -> int:
    output = 0
    for i in args:
        if isinstance(i, int):
            output += i
        else:
            output += sum_nested_ints(*i)
    return output
