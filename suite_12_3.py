import unittest
import tests_12_3 as hw1
import tests_12_3 as hw2
from unittest.runner import TextTestRunner


t_suite = unittest.TestSuite()


t_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(hw1.RunnerTest))
t_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(hw2.TournamentTest))


runner = TextTestRunner(verbosity=2)


runner.run(t_suite)