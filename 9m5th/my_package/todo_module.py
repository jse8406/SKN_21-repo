#my_package/todo_module.py

def summation(start:int, end:int) -> int:
    """
    Args:
        start (int): start integer to add 
        end (int): end integer to add

    Returns:
        int: sum of the integer in range start to the end
    """

    result = 0
    for v in range(start, end+1):
        result += v

    return result

print(summation(1, 10))
