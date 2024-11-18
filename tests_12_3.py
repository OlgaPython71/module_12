import unittest
from runner_and_tournament import Runner
from runner_and_tournament import Tournament


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_1 = Runner('Olga')
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_2 = Runner('Maxim')
        for _ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_3 = Runner('Denis')
        runner_4 = Runner('Elena')
        for _ in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEquals(runner_3.distance, runner_4.distance)


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner(name="Усэйн", speed=10)
        self.andrey = Runner(name="Андрей", speed=9)
        self.nick = Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f"{key}: {result}")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results["test_usain_nick"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results["test_andrey_nick"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results["test_usain_andrey_nick"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")


if __name__ == '__main__':
    unittest.main()
