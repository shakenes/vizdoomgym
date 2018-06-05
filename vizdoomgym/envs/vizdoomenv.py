import gym
from gym import spaces
from vizdoom import *
import numpy as np
import os
from gym.envs.classic_control import rendering

CONFIGS = [['basic.cfg', 3],                # 0
           ['deadly_corridor.cfg', 7],      # 1
           ['defend_the_center.cfg', 3],    # 2
           ['defend_the_line.cfg', 3],      # 3
           ['health_gathering.cfg', 3],     # 4
           ['my_way_home.cfg', 5],          # 5
           ['predict_position.cfg', 3],     # 6
           ['take_cover.cfg', 2],           # 7
           ['deathmatch.cfg', 20],          # 8
           ['health_gathering_supreme.cfg', 3]]  # 9


class VizdoomEnv(gym.Env):

    def __init__(self, level):

        # init game
        self.game = DoomGame()
        self.game.set_screen_resolution(ScreenResolution.RES_640X480)
        scenarios_dir = os.path.join(os.path.dirname(__file__), 'scenarios')
        self.game.load_config(os.path.join(scenarios_dir, CONFIGS[level][0]))
        self.game.set_window_visible(False)
        self.game.init()
        self.state = None

        self.action_space = spaces.Discrete(CONFIGS[level][1])
        self.observation_space = spaces.Box(0, 255, (self.game.get_screen_height(),
                                                     self.game.get_screen_width(),
                                                     self.game.get_screen_channels()),
                                            dtype=np.uint8)
        self.viewer = None

    def step(self, action):
        # convert action to vizdoom action space (one hot)
        act = np.zeros(self.action_space.n)
        act[action] = 1
        act = np.uint8(act)
        act = act.tolist()

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

    def render(self, mode='human'):
        try:
            img = self.game.get_state().screen_buffer
            img = np.transpose(img, [1, 2, 0])

            if self.viewer is None:
                self.viewer = rendering.SimpleImageViewer()
            self.viewer.imshow(img)
        except AttributeError:
            pass

    @staticmethod
    def get_keys_to_action():
        # you can press only one key at a time!
        keys = {(): 2,
                (ord('a'),): 0,
                (ord('d'),): 1,
                (ord('w'),): 3,
                (ord('s'),): 4,
                (ord('q'),): 5,
                (ord('e'),): 6}
        return keys
