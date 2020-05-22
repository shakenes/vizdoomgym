import unittest
import gym
import vizdoomgym


class BasicTest(unittest.TestCase):
    def test_basic(self):
        env = gym.make("VizdoomBasic-v0", test_arg="something")
        self.assertIsInstance(env, gym.Env)
        state = env.reset()
        self.assertEqual(len(state.shape), 3)
        state, reward, done, info = env.step(env.action_space.sample())
        self.assertEqual(len(state.shape), 3)
        self.assertIsNotNone(reward)
        self.assertIsInstance(done, bool)
        env.render()


if __name__ == "__main__":
    unittest.main()
