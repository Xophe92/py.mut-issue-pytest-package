def fibonacci(n: int) -> int:
    """
    Return the n-th element of the fibonacci sequence.
    Args:
        n (int): The fibonacci number to compute.
    Returns:
        Optional[int]: The n-th fibonacci number is n is positive int, None otherwise.
    """
    if not isinstance(n, int):
        raise TypeError(
            f'Fibonacci is only defined on integers, {type(n)} given.')
    if n <= 0:
        raise ValueError(
            f'Fibonacci is only defined on positive integers, {n} given.')
    if n <= 2:
        return (n)
    else:
        return fibonacci(n-1) + fibonacci(n-2)