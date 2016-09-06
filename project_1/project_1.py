"""
MCS 260 Project One by Rafeh Qazi
Modified: September 2016
Program: Calculate drainage time
"""
import math

# Gravity constant
G = 9.80665

# Welcome prompt
print('Hello, welcome to my drain time calculator!')

# Take in user input
a = float(input('Give the cross-sectional area of the hole the liquid is draining out of: '))
A = float(input('Give the horizontal cross-sectional area of the container: '))
H = float(input('Give the height of the liquid above the hole it is draining out of: '))

# Drain time formula
drain_time_secs = ((2 * A) / a) * math.sqrt((2 * H) / G)

# Use divmod to get quotient and remainder
minutes, seconds = divmod(drain_time_secs, 60)
hours, minutes = divmod(minutes, 60)

# Handle all string formatting cases of having seconds, minutes, or hours.
if seconds and minutes and hours:
    print('{} hours {} minutes and {} seconds'.format(int(hours), int(minutes), int(seconds)))

elif seconds and minutes:
    print('{} minutes and {} seconds'.format(int(minutes), int(seconds)))

elif minutes and hours:
    print('{} hours and {} minutes'.format(int(hours)), int(minutes))

elif seconds and hours:
    print('{} hours and {} seconds'.format(int(hours), int(seconds)))

elif hours:
    print('{} hours'.format(int(hours)))

elif minutes:
    print('{} minutes'.format(int(minutes)))

elif seconds:
    print('{} seconds'.format(int(seconds)))
