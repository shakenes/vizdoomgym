from vizdoomgym.envs.vizdoomenv import VizdoomEnv


class VizdoomTakeCover(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomTakeCover, self).__init__(7, **kwargs)
