__author__ = 'Rafeh'
"""
Modified: September 2016

Program: Scrabble

Scrabble Points Per Letter:
---------------------------------------------------------------------
1 point: E ×12, A ×9, I ×9, O ×8, N ×6, R ×6, T ×6, L ×4, S ×4, U ×4
2 points: D ×4, G ×3
3 points: B ×2, C ×2, M ×2, P ×2
4 points: F ×2, H ×2, V ×2, W ×2, Y ×2
5 points: K ×1
8 points: J ×1, X ×1
10 points: Q ×1, Z ×1
---------------------------------------------------------------------
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
    score = sum([SCRABBLE_POINTS[key] for letter in word for key in SCRABBLE_POINTS if letter in key])
    if len(word) >= 7:
        score += 50
    return score
