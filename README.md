# vizdoomgym
This is a wrapper to use [ViZDoom](https://github.com/mwydmuch/ViZDoom "ViZDoom repository") together with [OpenAI Gym](https://github.com/openai/gym "OpenAI Gym repository"). 

## Installation

```
git clone https://github.com/simontudo/vizdoomgym.git
cd vizdoomgym
pip install -e .
```

Use one of the environments (see list below for all available envs):
```
import gym
import vizdoomgym
env = gym.make('VizdoomBasic-v0')
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
