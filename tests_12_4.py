import logging
import unittest
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding='UTF-8', format='%(asctime)s - %(levelname)s - %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            logging.info('"test_walk" выполнен успешно')
            runner_1 = Runner('Olga')
            for _ in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, -5)
        except Exception as e:
            logging.warning('Неверная скорость для Runner')
            return e

    def test_run(self):
        try:
            logging.info('"test_run" выполнен успешно')
            runner_2 = Runner(25)
            for _ in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
        except Exception as e:
            logging.warning('Неверный тип данных для объекта Runner')
            return e
