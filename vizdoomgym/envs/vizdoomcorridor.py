from vizdoomgym.envs.vizdoomenv import VizdoomEnv


class VizdoomCorridor(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomCorridor, self).__init__(1, **kwargs)
