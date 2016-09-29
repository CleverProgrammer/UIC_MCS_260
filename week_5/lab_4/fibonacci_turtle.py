"""
Lab 4 by Rafeh Qazi
"""
import turtle


def fibonacci(n):
    """
    :param n: int
    :return: int

    >>> fibonacci(5)
    5
    >>> fibonacci(1)
    1
    >>> fibonacci(3)
    2
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_spiral(n):
    my_turtle = turtle.Turtle()
    my_turtle.setheading(50)
    for i in range(n):
        my_turtle.circle(fibonacci(i), extent=90)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    fibonacci_spiral(int(input("How many fibonacci spirals would you like to make? ")))
