def add(*args) -> float:
    """
    Add two numbers.
    Parameters:
        x1 (float): The first number.
        x2 (float): The second number.
    Returns:
        float: The sum of the two numbers.
    """
    for arg in args:
        if not isinstance(arg, (int, float)):
            return None
    return sum(args)


def subtract(x1: float, x2: float) -> float:
    """
    Subtract two numbers.

    Parameters:
        x1 (float): The first number.
        x2 (float): The second number.
    Returns:
        float: The difference of the two numbers.
    """
    if not isinstance(x1, (int, float)) or not isinstance(x2, (int, float)):
        return None
    else:
        return x1 - x2


def multiply(*args) -> float:
    """
    Multiply two numbers.

    Parameters:
        x1 (float): The first number.
        x2 (float): The second number.
    Returns:
        float: The product of the two numbers.
    """
    for arg in args:
        if not isinstance(arg, (int, float)):
            return None
    product = 1
    for n in args:
        product *= n
        

def divide(x1: float, x2: float) -> float:
    """
    Divide two numbers.
    Parameters:
        x1 (float): The first number.
        x2 (float): The second number.
    Returns:
        float: The quotient of the two numbers.
    """
    if not isinstance(x1, (int, float)) or not isinstance(x2, (int, float)):
        return None
    else:
        if x2 == 0:
            return None
        else:
            return x1 / x2
