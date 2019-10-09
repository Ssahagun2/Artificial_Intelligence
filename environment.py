""""
Instance variables:
status: The state (dictionary) of the locations in the Environment, squares A and B, and whether they are
        Dirty or Clean. Initialized upon creation to a random choice from Dirty or Clean.
agent_location: The current location of the agent. Initialized to a random location chosen from squares A and B -
                gets updated as the agent moves.
agent: The Agent that is currently moving around the Environment.

Class variables:
ACTIONS: Maps the agent action to a location.

Saul Sahagun
Cs 335-1, Fall 2019
"""
import random


class Environment:
    ACTIONS = {'Right': 'B', 'Left': 'A'}

    def __init__(self, agent):
        self.status = {
            'A': random.choice(['Dirty', 'Clean']),
            'B': random.choice(['Dirty', 'Clean'])
        }
        self.agent_location = random.choice(list(self.status.keys()))
        self.agent = agent

    def execute_program(self, time):
        loc = self.agent_location
        curStat = self.status[self.agent_location]
        while time > 0:
            action = self.agent.program(loc, curStat)
            if action == 'Suck':
                curStat = 'Clean'
                self.agent.program(loc, curStat)
            else:
                self.agent.performance += 1
                self.agent_location = Environment.ACTIONS[action]
            time -= 1
