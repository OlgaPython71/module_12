import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = Runner('Olga')
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = Runner('Maxim')
        for _ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = Runner('Denis')
        runner_4 = Runner('Elena')
        for _ in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEquals(runner_3.distance, runner_4.distance)


if __name__ == '__main__':
    unittest.main()
