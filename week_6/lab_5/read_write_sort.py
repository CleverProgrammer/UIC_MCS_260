"""
Author: Rafeh Qazi
Course: MCS 260 at UIC (Intro CS)
Modified: October 2016
Program: Worksheet 6
"""


def best_way_to_read_file(file_name):
    """This is the best way, other ways kind of suck and are not pythonic. """

    # with open is a context processor so no need to open or close files.
    # https://www.python.org/dev/peps/pep-0343/
    with open(file_name, 'r') as f:
        for line in f:
            print(line)


# example with .read()
file_name = 'things_to_sort'
with open(file_name, 'r') as f:
    # f.read() reads the entire file all at once.
    # all read* methods are intrinsically generators. They yield rather than return.
    print(f.read())
    print(f.readline())
    print(f.readlines())

# if you want to get the content again, re-open the file.
# ex: with open(file_name, 'r') as f...
with open('things_to_sort', 'r') as f:
    lines = [char.strip() for char in f]
    new_lines = [elem.split(', ') for elem in lines]
    integers = list(sorted(map(int, (char for elem in new_lines for char in elem if char.isdigit()))))
    strings = list(sorted((char for elem in new_lines for char in elem if char.isalpha())))
    print(integers)
    print(strings)

with open('sorted_things.txt', 'w') as f:
    f.write(', '.join(map(str, integers)) + '\n')
    f.write(', '.join(strings))
