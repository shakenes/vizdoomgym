from vizdoomgym.envs.vizdoomenv import VizdoomEnv


class VizdoomDefendCenter(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomDefendCenter, self).__init__(2, **kwargs)
