from vizdoomgym.envs.vizdoomenv import VizdoomEnv


class VizdoomBasic(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomBasic, self).__init__(0, **kwargs)
