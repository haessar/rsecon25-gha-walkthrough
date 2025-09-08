from typing import Union, Iterable

import numpy as np

def _flatten(arr, typ=int):
    for x in arr:
        if isinstance(x, typ):
            yield x
        else:
            yield from _flatten(x, typ)

def sum_nested_ints(*args: Union[Iterable, int]) -> int:
    """
    Calculate sum of all ints passed as args,
    regardless of level of nesting
    """
    ints = np.array(list(_flatten(args)))
    if not np.isdtype(ints.dtype, np.int64):
        raise TypeError("Expected integer dtype")
    return ints.sum()
