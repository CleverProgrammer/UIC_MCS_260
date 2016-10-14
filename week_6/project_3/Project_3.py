"""
MCS 260 Project Three by Rafeh Qazi
Modified: October 2016
Program: Create a word cloud that visualizes the word frequencies.
"""
import string
import turtle
from collections import Counter


def save_data_string(string):
    """Write to a file."""

    with open('data_file.txt', 'w') as f:
        f.writelines(string)


def print_data():
    """Read data from a file."""

    with open('data_file.txt', 'r') as f:
        for line in f:
            print(line)


def remove_punc(in_string):
    """Remove all punctuation from string."""

    exclude = set(string.punctuation)
    out_string = ''.join(ch for ch in in_string if ch not in exclude)
    return out_string.lower()


def word_freq_dict():
    """Return a word frequency dictionary."""

    with open('data_file.txt', 'r') as f:
        lines = [remove_punc(line.strip()).split() for line in f]

    word_freq = Counter()
    for line in lines:
        word_freq += Counter(line)

    return word_freq


def word_tower():
    word_freq = word_freq_dict()
    total = sum(word_freq.values())
    counter = 0
    t = turtle.Turtle()
    t.up()
    t.goto(0, -250)
    t.left(90)
    for word in word_freq:
        counter += 15
        t.hideturtle()
        t.write(word, font=('Ariel', word_freq[word] * 10, 'normal'))
        t.forward(word_freq[word] / total * 100 * 3.5)

    turtle.done()


if __name__ == '__main__':
    save_data_string(input('Enter file content here: '))
    print_data()
    word_tower()
