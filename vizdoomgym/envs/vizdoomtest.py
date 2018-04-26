import gym
from gym import spaces


class VizdoomTest(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(0, 255, (300, 200, 3))
        self.reward_range = (0, 1)

    def step(self, action):
        pass
        # return observation, reward, done, info

    def reset(self):
        pass
        # return observation

    def render(self, mode='human', close=False):
        pass
