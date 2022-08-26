from season import number_of_minuts
import unittest
from unittest.mock import patch

from jar import Jar


class TestSeason(unittest.TestCase):
    def test_number_of_minuts_error(self):
        with self.assertRaises(ValueError):
            number_of_minuts("January 1, 1999")


class TestJar(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(ValueError):
            Jar(-2)

        obj=Jar()
        assert obj.capacity == 12

    def test_str(self):
        jar = Jar()
        assert str(jar) == ""
        jar.deposit(1)
        assert str(jar) == "🍪"
        jar.deposit(11)
        assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    def test_deposit(self):
        jar = Jar()
        jar.deposit(2)
        assert jar.size == 2
        with self.assertRaises(ValueError):
            jar.deposit(13)


    def test_withdraw(self):
        obj=Jar()
        obj.size =10
        obj.withdraw(2)
        assert obj.size == 8

        with self.assertRaises(ValueError):
            obj.withdraw(20)


