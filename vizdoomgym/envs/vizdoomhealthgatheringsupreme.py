from vizdoomgym.envs.vizdoomenv import VizdoomEnv


class VizdoomHealthGatheringSupreme(VizdoomEnv):
    def __init__(self, **kwargs):
        super(VizdoomHealthGatheringSupreme, self).__init__(9, **kwargs)
