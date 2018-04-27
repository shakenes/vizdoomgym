# vizdoomgym

## Installation

```
git clone https://github.com/simontudo/vizdoomgym.git
cd vizdoomgym
pip install -e .
```

Use the test environment:
```
import gym
import vizdoomgym
env = gym.make('VizdoomTest-v0')
```

Available environments (for information about the environments take a look at https://github.com/simontudo/vizdoomgym/blob/master/vizdoomgym/envs/scenarios/README.md)
```
VizdoomBasic-v0
VizdoomCorridor-v0
VizdoomDefendCenter-v0
VizdoomDefendLine-v0
VizdoomHealthGathering-v0
VizdoomMyWayHome-v0
VizdoomPredictPosition-v0
VizdoomTakeCover-v0
```
