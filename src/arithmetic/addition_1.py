import numpy as np

def _flatten(arr, typ=int):
    for x in arr:
        if isinstance(x, typ):
            yield x
        else:
            yield from _flatten(x, typ)

def sum_nested_ints(*args: int) -> int:
    ints = np.fromiter(_flatten(args), dtype=np.int64)
    if not np.isdtype(ints.dtype, np.integer):
        raise TypeError("Expected integer dtype")
    return ints.sum()
