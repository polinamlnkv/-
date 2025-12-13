# test_singleton_tdd.py
import unittest
from singleton import Singleton

class TestSingleton(unittest.TestCase):
    def test_single_instance(self):
        s1 = Singleton()
        s2 = Singleton()
        self.assertIs(s1, s2)

    def test_value_property(self):
        s1 = Singleton()
        s1.set_value(42)
        s2 = Singleton()
        self.assertEqual(s2.get_value(), 42)

if __name__ == "__main__":
    unittest.main()
