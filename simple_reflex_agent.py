"""
Instance variables:
performance: Performance of the agent

Class variables:
RULES: Maps the status of the environment to an action

Saul Sahagun
Cs 335-1, Fall 2019
"""


class SimpleReflexAgent:
    RULES = {'A': 'Right', 'B': 'Left'}

    def __init__(self):
        self.performance = 0

    @staticmethod
    def program(loc, status):
        if status == 'dirty':
            s = 'suck'
        else:
            s = SimpleReflexAgent.RULES[loc]
            if s == 'A':
                s = 'Right'
            else:
                s = 'Left'
        return s
