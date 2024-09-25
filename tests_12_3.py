import unittest

from test_runner import Runner
from test_tournament import Tournament


def skip_frozen(test_method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return test_method(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'пропуск')
    def test_walk(self, name='John'):
        obj_1 = Runner(name)
        for _ in range(10):
            obj_1.walk()
        self.assertEqual(obj_1.distance, 50)

    @unittest.skipIf(is_frozen, 'пропуск')
    def test_run(self, name='Jane'):
        obj_2 = Runner(name)
        for _ in range(10):
            obj_2.run()
        self.assertEqual(obj_2.distance, 100)

    @unittest.skipIf(is_frozen, 'пропуск')
    def test_challenge(self, name='John'):
        obj_1 = Runner(name)
        obj_2 = Runner(name='Jane')
        for _ in range(10):
            obj_1.run()
            obj_2.walk()
        self.assertNotEqual(obj_1.distance, obj_2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.obj_1 = Runner("Усэйн", speed=10)
        self.obj_2 = Runner("Андрей", speed=9)
        self.obj_3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)

    @unittest.skipIf(is_frozen, 'пропуск')
    def test_1(self):
        trn = Tournament(90, self.obj_1, self.obj_3)
        result = trn.start()
        self.all_results[1] = result
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")

    @unittest.skipIf(is_frozen, 'пропуск')
    def test_2(self):
        trn = Tournament(90, self.obj_2, self.obj_3)
        result = trn.start()
        self.all_results[2] = result
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")

    @unittest.skipIf(is_frozen, 'пропуск')
    def test_3(self):
        trn = Tournament(90, self.obj_1, self.obj_2, self.obj_3)
        result = trn.start()
        self.all_results[3] = result
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")

if __name__ == '__main__':
    unittest.main()