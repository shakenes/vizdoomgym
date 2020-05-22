from vizdoomgym.envs.vizdoomenv import VizdoomEnv


class VizdoomPredictPosition(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomPredictPosition, self).__init__(6, **kwargs)
