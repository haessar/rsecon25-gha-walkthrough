def sum_nested_ints(*args: int) -> int:
    output = 0
    for i in args:
        if isinstance(i, int):
            output += i
        else:
            output += sum_nested_ints(*i)
    return output
