from vizdoomgym.envs.vizdoomenv import VizdoomEnv


class VizdoomDeathmatch(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomDeathmatch, self).__init__(8, **kwargs)
