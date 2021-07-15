# ViZDoomGym ![](https://github.com/shakenes/vizdoomgym/workflows/perform_tests/badge.svg)
This is a wrapper to use [ViZDoom](https://github.com/mwydmuch/ViZDoom "ViZDoom repository"), a "Doom based AI Research Platform for Reinforcement Learning from Raw Visual Information" together with [OpenAI Gym](https://github.com/openai/gym "OpenAI Gym repository").

There is a branch with an alternative reward system for the Health Gathering scenario (each collected health pack yields +1 reward)

## Installation

```
sudo apt-get install cmake libboost-all-dev libgtk2.0-dev libsdl2-dev python-numpy
git clone https://github.com/shakenes/vizdoomgym.git
cd vizdoomgym
pip install -e .
```
## Usage
Use one of the environments (see list below for all available envs):
```
import gym
import vizdoomgym
env = gym.make('VizdoomBasic-v0', **kwargs)

# use like a normal Gym environment
state = env.reset()
state, reward, done, info = env.step(env.action_space.sample())
env.render()
env.close()
```

### Possible observations
It is possible to get the depth buffer, the labels buffer, the player's position and viewing angle and the player's health as additional observations. If more than one observation is provided, the observations are returned as a list of numpy array (or floats, respectively). 
```
env = gym.make('VizdoomBasic-v0, depth=True, labels=True, position=True, health=True)
```


### List of available environments
```
VizdoomBasic-v0
VizdoomCorridor-v0
VizdoomDefendCenter-v0
VizdoomDefendLine-v0
VizdoomHealthGathering-v0
VizdoomMyWayHome-v0
VizdoomPredictPosition-v0
VizdoomTakeCover-v0
VizdoomDeathmatch-v0
VizdoomHealthGatheringSupreme-v0
```

[Detailed information about the environments](https://github.com/shakenes/vizdoomgym/blob/master/vizdoomgym/envs/scenarios/README.md)

## Future plans
- Support for more GameVariables such as health through kwargs
- Provide more options for the observations (player position, health...)
- Use a dictionary for all the observations

Ideas for new features and of course PRs are always welcome!
