import gym
from gym import spaces


class VizdoomTest(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        print("Hello World!")
        pass

    def step(self, action):
        pass
        # return observation, reward, done, info

    def reset(self):
        pass
        # return observation

    def render(self, mode='human', close=False):
        pass
