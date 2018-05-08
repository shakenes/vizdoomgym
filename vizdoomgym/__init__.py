from gym.envs.registration import register

register(
    id='VizdoomBasic-v0',
    entry_point='vizdoomgym.envs:VizdoomBasic'
)

register(
    id='VizdoomCorridor-v0',
    entry_point='vizdoomgym.envs:VizdoomCorridor'
)

register(
    id='VizdoomDefendCenter-v0',
    entry_point='vizdoomgym.envs:VizdoomDefendCenter'
)

register(
    id='VizdoomDefendLine-v0',
    entry_point='vizdoomgym.envs:VizdoomDefendLine'
)

register(
    id='VizdoomHealthGathering-v0',
    entry_point='vizdoomgym.envs:VizdoomHealthGathering'
)

register(
    id='VizdoomMyWayHome-v0',
    entry_point='vizdoomgym.envs:VizdoomMyWayHome'
)

register(
    id='VizdoomPredictPosition-v0',
    entry_point='vizdoomgym.envs:VizdoomPredictPosition'
)

register(
    id='VizdoomTakeCover-v0',
    entry_point='vizdoomgym.envs:VizdoomTakeCover'
)

register(
    id='VizdoomDeathmatch-v0',
    entry_point='vizdoomgym.envs:VizdoomDeathmatch'
)

register(
    id='VizdoomHealthGatheringSupreme-v0',
    entry_point='vizdoomgym.envs:VizdoomHealthGatheringSupreme'
)
