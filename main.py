import gymnasium as gym
from gymnasium import spaces
import numpy as np
import random


class CreditCardEnv(gym.Env):

    def __init__(self):
        super(CreditCardEnv, self).__init__()
        # Observation space: (4 face down cards, 1 drawn card, discard pile top card)
        self.observation_space = spaces.Box(low=1, high=10, shape=(6,), dtype=np.int32)
        """
        Action space:
        0 = Draw deck
        1 = Pick discard
        2-5 = Swap with cards 1-4
        6 = Discard
        7 = Call credit card
        """
        self.action_space = spaces.Discrete(8)
        self.reset()

    def reset(self, seed=None, options=None):
        self.deck = list(range(1, 11)) * 4  # A deck with values 1 - 10
        random.shuffle(self.deck)
        self.player_cards = [self.deck.pop() for _ in range(4)]
        self.opponent_cards = [self.deck.pop() for _ in range(4)]
        self.discard_pile = [self.deck.pop()]
        self.current_card = None
        self.game_over = False
        self.called_credit_card = False
        self.swap_stage = 0
        return np.array(self.player_cards + [self.current_card or 0, self.discard_pile[-1] if self.discard_pile else 0]), {}

    def step(self, action):
        """Executes an action in the environment"""
        reward = 0
        done = False

        if self.current_card is None:
            if action == 0:
                if self.deck:
                    self.current_card = self.deck.pop()
            elif action == 1:
                if self.discard_pile:
                    self.current_card = self.discard_pile.pop()
        else:
            if self.swap_stage < 4:
                if action == 2:
                    self.player_cards[self.swap_stage], self.current_card = (
                        self.current_card,
                        self.player_cards[self.swap_stage],
                    )
                    self.swap_stage += 1
            elif action == 3:
                self.discard_pile.append(self.current_card)
                self.current_card = None
                self.swap_stage = 0
            elif action == 4:
                self.called_credit_card = True
                done = True

        # Compute reward at end of turn
        if done:
            player_score = sum(self.player_cards)
            opponent_score = sum(self.opponent_cards)

            if player_score < opponent_score:
                reward = 10
            else:
                reward = -10

        # Ensure discard pile access doesn't fail
        discard_top = self.discard_pile[-1] if self.discard_pile else 0

        return np.array(self.player_cards + [self.current_card or 0, discard_top]), reward, done, False, {}

    def render(self):
        print(f"Player Cards: {self.player_cards}, Current Card: {self.current_card}, Discard Pile: {self.discard_pile[-1]}")


def main():
    from stable_baselines3 import PPO
    env = CreditCardEnv()
    model = PPO("MlpPolicy", env, verbose=1, device="cuda")
    model.learn(total_timesteps=100_000)
    model.save("credit_card_ppo")


if __name__ == "__main__":
    main()