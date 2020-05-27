import unittest
import gym
import vizdoomgym
import numpy as np


class BasicTest(unittest.TestCase):
    def test_basic(self):
        env = gym.make("VizdoomBasic-v0")
        self.assertFalse(env.unwrapped.depth)
        self.assertFalse(env.unwrapped.labels)
        self.assertIsInstance(env, gym.Env)
        state = env.reset()
        self.assertEqual(len(state.shape), 3)
        self.assertIsInstance(state, np.ndarray)
        self.assertTrue(state.shape, env.observation_space.shape)
        done = False
        while not done:
            state, reward, done, info = env.step(env.action_space.sample())
            self.assertEqual(len(state.shape), 3)
            self.assertIsInstance(state, np.ndarray)
            self.assertTrue(state.shape, env.observation_space.shape)
            self.assertIsNotNone(reward)
            self.assertIsInstance(done, bool)
            env.render()
        env.close()

    def test_kwargs(self):
        env = gym.make("VizdoomHealthGathering-v0", depth=True, labels=True)
        self.assertTrue(env.unwrapped.depth)
        self.assertTrue(env.unwrapped.labels)
        self.assertIsInstance(env, gym.Env)
        state = env.reset()
        self.assertEqual(len(state), 3)
        self.assertTrue(all(isinstance(s, np.ndarray) for s in state))
        done = False
        while not done:
            state, reward, done, info = env.step(env.action_space.sample())
            self.assertEqual(len(state), 3)
            self.assertTrue(all(isinstance(s, np.ndarray) for s in state))
            self.assertTrue(
                all(
                    s.shape == env.observation_space[i].shape
                    for i, s in enumerate(state)
                )
            )
            self.assertIsNotNone(reward)
            self.assertIsInstance(done, bool)
            env.render()
        env.close()

    def test_health_and_position(self):
        env = gym.make("VizdoomHealthGathering-v0", health=True, position=True)
        self.assertIsInstance(env, gym.Env)
        state = env.reset()
        self.assertEqual(len(state), 3)
        self.assertTrue(all(isinstance(s, (np.ndarray, np.float64)) for s in state))
        done = False
        while not done:
            state, reward, done, info = env.step(env.action_space.sample())
            self.assertEqual(len(state), 3)
            self.assertTrue(all(isinstance(s, (np.ndarray, np.float64)) for s in state))
            self.assertTrue(
                all(
                    s.size == np.prod(env.observation_space[i].shape)
                    for i, s in enumerate(state)
                )
            )
            self.assertIsNotNone(reward)
            self.assertIsInstance(done, bool)
            env.render()
        env.close()

    def test_all(self):
        env = gym.make(
            "VizdoomHealthGathering-v0",
            depth=True,
            labels=True,
            health=True,
            position=True,
        )
        self.assertIsInstance(env, gym.Env)
        state = env.reset()
        self.assertEqual(len(state), 5)
        self.assertTrue(all(isinstance(s, (np.ndarray, np.float64)) for s in state))
        done = False
        while not done:
            state, reward, done, info = env.step(env.action_space.sample())
            self.assertEqual(len(state), 5)
            self.assertTrue(all(isinstance(s, (np.ndarray, np.float64)) for s in state))
            self.assertTrue(
                all(
                    s.size == np.prod(env.observation_space[i].shape)
                    for i, s in enumerate(state)
                )
            )
            self.assertIsNotNone(reward)
            self.assertIsInstance(done, bool)
            env.render()
        env.close()


if __name__ == "__main__":
    unittest.main()
