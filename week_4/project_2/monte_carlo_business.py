"""
MCS 260 Project Two by Rafeh Qazi
Modified: September 2016
Program: Calculate average hourly maximum customer volume.
"""

import numpy
from collections import Counter
from random import randrange


def ave_max_calc(C, H, D):
    """
    Simulates a business with customers, hours, and days.
    Outputs the average max hourly customer volume.
    """
    # Counter for getting most common, numpy for averaging, and loops for given customers and days.
    return numpy.mean([Counter([randrange(0, H) for _ in range(C)]).most_common()[0][1] for _ in range(D)])


if __name__ == '__main__':
    print("Hello, welcome to my average maximum hourly customer value calculator!")
    C = int(input("Give me the number of customers per day: "))
    H = int(input("Give me the number of business hours per day: "))
    D = int(input("Give me the number of days to simulate: "))

    print(ave_max_calc(C, H, D))
