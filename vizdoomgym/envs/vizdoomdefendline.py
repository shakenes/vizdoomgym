from vizdoomgym.envs.vizdoomenv import VizdoomEnv


class VizdoomDefendLine(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomDefendLine, self).__init__(3, **kwargs)
