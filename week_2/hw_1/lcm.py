"""
Author: Rafeh Qazi
Program: Least common multiple
Modified: September 2016
"""

def lcm(a, b):
    """
    Find the least common multiple between 2 numbers.

    :param a: int
    :param b: int
    :return: int

    >>> lcm(6, 10)
    30

    >>> lcm(234,346)
    40482
    """
    set_a = {a}
    set_b = {b}
    n = 1
    while not set_a & set_b:
        set_a.add(a*n)
        set_b.add(b*n)
        n += 1
    return (set_a & set_b).pop()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
