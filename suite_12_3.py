import unittest
import tests_12_3


test12 = unittest.TestSuite()
test12.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test12.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(test12)
