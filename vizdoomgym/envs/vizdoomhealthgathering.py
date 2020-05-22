from vizdoomgym.envs.vizdoomenv import VizdoomEnv


class VizdoomHealthGathering(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomHealthGathering, self).__init__(4, **kwargs)
