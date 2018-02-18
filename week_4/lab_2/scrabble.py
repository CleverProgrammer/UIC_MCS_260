__author__ = 'Rafeh'
"""
Modified: September 2016

Program: Scrabble

Scrabble Points Per Letter:
---------------------------------------------------------------------
1 point: E, A, I, O, N, R, T, L, S, U
2 points: D, G
3 points: B, C, M, P
4 points: F, H, V, W, Y
5 points: K
8 points: J, X
10 points: Q, Z
---------------------------------------------------------------------

50 Point Bonus: If the length of a word is 7 letters or more.
"""
SCRABBLE_POINTS = {
    'eaionrtlsu': 1,
    'dg': 2,
    'bcmp': 3,
    'fhvwy': 4,
    'k': 5,
    'jx': 8,
    'qz': 10
}

def scrabble(word):
    """
    >>> scrabble('equalize')
    76
    :param word: str
    :return: int
    """
    score = sum([SCRABBLE_POINTS[key] for letter in word for key in SCRABBLE_POINTS if letter in key])
    if len(word) >= 7:
        score += 50
    return score
