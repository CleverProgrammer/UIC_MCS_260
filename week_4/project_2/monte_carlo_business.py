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
    return numpy.mean([Counter([randrange(0, H) for _ in range(C)]).most_common()[0][1] for _ in range(D)])
