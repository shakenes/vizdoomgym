import unittest
import gym
import vizdoomgym


class BasicTest(unittest.TestCase):
    def test_basic(self):
        env = gym.make("VizdoomBasic-v0")
        self.assertIsInstance(env, gym.Env)
        state = env.reset()
        self.assertEqual(len(state.shape), 3)
        self.assertTrue(state.shape, env.observation_space.shape)
        state, reward, done, info = env.step(env.action_space.sample())
        self.assertEqual(len(state.shape), 3)
        self.assertTrue(state.shape, env.observation_space.shape)
        self.assertIsNotNone(reward)
        self.assertIsInstance(done, bool)
        env.render()
        env.close()

    def test_kwargs(self):
        env = gym.make("VizdoomDefendCenter-v0", object_labels=True)
        # self.assertTrue(env.unwrapped.object_labels)
        self.assertIsInstance(env, gym.Env)
        state = env.reset()
        self.assertEqual(len(state.shape), 3)
        self.assertTrue(state.shape, env.observation_space.shape)
        state, reward, done, info = env.step(env.action_space.sample())
        self.assertEqual(len(state.shape), 3)
        self.assertTrue(state.shape, env.observation_space.shape)
        self.assertIsNotNone(reward)
        self.assertIsInstance(done, bool)
        env.render()
        env.close()


if __name__ == "__main__":
    unittest.main()
