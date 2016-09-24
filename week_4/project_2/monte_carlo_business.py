from random import randrange


def count_common(my_list):
    """
    The number of times the most common element occurs in a list.
    :param my_list: list
    :return: int

    >>> count_common([1, 1])
    2
    >>> count_common([1, 2, 2, 1, 2])
    3
    """
    max_num = my_list.count(my_list[-1])
    for element in my_list:
        if my_list.count(element) > max_num:
            max_num = my_list.count(element)
    return max_num


def ave_max_calc(C, H, D):
    """
    Simulates a business with customers, hours, and days.
    Outputs the average max hourly customer volume.
    :param C: int
    :param H: int
    :param D: int
    :return: float
    """
    busy_max = []
    for _ in range(D):
        customers = []
        for i in range(C):
            customers.append(randrange(0, H))
        busy_max.append(count_common(customers))

    return sum(busy_max) / len(busy_max)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
