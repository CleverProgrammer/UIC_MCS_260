"""
Author: Rafeh Qazi.
Class: MCS 260 at UIC.
Date Modified: November 3rd.
Program: Voting Simulation.
"""
import random


class State:
    senators = 4

    def __init__(self, population, party):
        self.population = population
        self.senators = 4
        self.party = party
        # .1% of the population? Perhaps the worksheet means 1% of the population?
        self.representatives = 0.001 * population
        # try:
        #     assert self.percent_in_party1 + self.percent_in_party2 + self.percent_in_party3 + self.percent_in_party4 <= 1
        #     self.percent_in_party1 = None
        #     self.percent_in_party2 = None
        #     self.percent_in_party3 = None
        #     self.percent_in_party4 = None
        # except AssertionError:
        #     print('Sum of all party percentages should add up to 1.')

    # http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
    @staticmethod
    def weighted_choice(choices):
        total = sum(w for c, w in choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in choices:
            if upto + w >= r:
                return c
            upto += w
        assert False, "Shouldn't get here"

    def electoral_votes(self):
        return self.senators + self.representatives

    def voting(self, probability):
        choices = []
        parties = range(1, 5)
        for party in parties:
            if not party == self.party:
                choices.append((party, .5))
            else:
                choices.append((self.party, probability))

        return self.weighted_choice(choices)


class Type1(State):
    pass

dude = State(100, 2)
print(dude.voting(probability=5))
