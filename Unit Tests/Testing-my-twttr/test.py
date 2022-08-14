import unittest
from twttr import shorten
from home_Federal_Savings_Bank import bank
from fuel_guage import convert,gauge


def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"


def test_bank():
    assert bank("hello") == 100
    assert bank("hey") == 20
    assert bank("good morning") == 0


def test_bank_capital():
    assert bank("HeLLo") == 100
    assert bank("HEY") == 20


def test_bank_whitespace():
    assert bank(" hello ") == 100
    assert bank(" hey ") == 20


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50


def test_convert_whitespace():
    assert convert(" 3/4 ") == 75
    assert convert(" 1/2 ") == 50

def test_gauge():
    assert gauge(34) == "34%"
    assert gauge(50) == "50%"

def test_gauge_full_empty():
    assert gauge(1) == "E"
    assert gauge(99) == "F"

class Error_test(unittest.TestCase):

    def test_convert_witchot_slash(self):
        self.assertRaises(ValueError,convert,"34")
        self.assertRaises(ValueError,convert,"12")

    def test_convert_wrong_numbers(self):
        self.assertRaises(ZeroDivisionError, convert, "3/0")
        self.assertRaises(ValueError, convert, "2/1")

    def test_guage_wrong_numbers(self):
        self.assertRaises(ValueError, gauge, 110)




