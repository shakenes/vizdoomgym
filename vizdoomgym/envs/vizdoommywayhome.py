from vizdoomgym.envs.vizdoomenv import VizdoomEnv


class VizdoomMyWayHome(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomMyWayHome, self).__init__(5, **kwargs)
