import gym
from gym import spaces
from vizdoom import *
import numpy as np
import os

CONFIGS = ['basic.cfg',
           'deadly_corridor.cfg',
           'defend_the_center.cfg',
           'defend_the_line.cfg',
           'health_gathering.cfg',
           'my_way_home.cfg',
           'predict_position.cfg',
           'take_cover']


class VizdoomEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, level):
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(0, 255, (240, 320, 3))
        self.reward_range = (0, 1)

        # init game
        self.game = DoomGame()
        self.game.set_screen_resolution(ScreenResolution.RES_640X480)
        scenarios_dir = os.path.join(os.path.dirname(__file__), 'scenarios')
        self.game.load_config(os.path.join(scenarios_dir, CONFIGS[level]))
        self.game.init()
        self.state = None

    def step(self, action):
        if action == 0:
            act = [0, 0, 1]
        elif action == 1:
            act = [1, 0, 0]
        else:
            act = [0, 1, 0]

        reward = self.game.make_action(act)
        state = self.game.get_state()
        done = self.game.is_episode_finished()
        if not done:
            observation = np.transpose(state.screen_buffer, (1, 2, 0))
        else:
            observation = np.uint8(np.zeros(self.observation_space.shape))

        info = {'dummy': 0}

        return observation, reward, done, info

    def reset(self):
        self.game.new_episode()
        self.state = self.game.get_state()
        img = self.state.screen_buffer
        return np.transpose(img, (1, 2, 0))

    def render(self, mode='human', close=False):
        pass
