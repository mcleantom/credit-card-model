import gymnasium as gym
import numpy as np



class CreditCardPlayer:

    def __init__(self):
        self.cards = [None, None, None, None]
        self.current_card = None
        self.swap_stage = 0

    def play(self, action: int):
        pass


class CreditCardGame(gym.Env):

    def __init__(self):
        self.model_player = CreditCardPlayer()
        self.model_opponent = CreditCardPlayer()
        self.current_turn = "player"
        self.discard_pile = []
        self.swap_stage = 0
        self.opponent_swap_stage = 0
        self.called_credit_card = False
        self.deck = list(range(1, 53))
        np.random.shuffle(self.deck)

    def reset(self, seed=None, options=None):
        """Reset the game for a new episode"""
        self.model_player = CreditCardPlayer()
        self.model_opponent = CreditCardPlayer()
        self.discard_pile = []
        self.swap_stage = 0
        self.opponent_swap_stage = 0
        self.called_credit_card = False
        self.deck = list(range(1, 53))
        np.random.shuffle(self.deck)

    def step(self, action):
        reward = 0
        done = False

        if self.current_turn == "player":
            pass

        if self.current_turn == "opponent":
            pass

        if done:
            pass

        self.current_turn = "opponent" if self.current_turn == "player" else "player"

