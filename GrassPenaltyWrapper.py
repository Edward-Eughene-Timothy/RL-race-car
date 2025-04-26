import gymnasium as gym
import numpy as np
from gymnasium import Wrapper

class GrassPenaltyWrapper(Wrapper):
    def __init__(self, env, penalty=-5.0, green_threshold=150, green_ratio=0.2):
        super().__init__(env)
        self.penalty = penalty
        self.green_threshold = green_threshold
        self.green_ratio = green_ratio

    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)

        # Check for green (grass) pixels — high green channel
        green_pixels = obs[:, :, 1] > self.green_threshold
        green_ratio = np.mean(green_pixels)

        if green_ratio > self.green_ratio:
            reward += self.penalty  # Apply soft penalty

        return obs, reward, terminated, truncated, info
