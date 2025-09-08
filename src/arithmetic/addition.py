def sum_nested_ints(*args: int) -> int:
    """
    Calculate sum of all ints passed as args,
    regardless of level of nesting
    """
    output = 0
    for i in args:
        if isinstance(i, int):
            output += i
        else:
            output += sum_nested_ints(*i)
    return output
