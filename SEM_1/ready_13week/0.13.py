from math import pi
import unittest

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("positive radius expected")
        self.radius = radius

    def area(self):
        assert self.radius >= 0, "positive radius expected"
        print(pi * self.radius ** 2)
        return pi * self.radius ** 2

    def correct_radius(self, correction_coefficient):
        self.radius *= correction_coefficient
        print(self.radius)

tire = Circle(42)
tire.area()

tire.correct_radius(1.02)
tire.area()

number = 10
assert isinstance(number, (int, float))
assert number > 0, "number should be > 0"

#number = -10
#assert isinstance(number, (int, float))
#assert number > 0, "number should be > 0"

assert 3 > 2
#assert 3 < 2

#assert 3 == 2

assert 3 > 2 and 4 > 3
#assert 3 < 2 or 4 < 3

numbers = [1, 2, 3, 4]
assert 2 in numbers
#assert 10 in numbers

assert not 10 in numbers

x = 1
y = x
z = None

assert x is y
assert z is None
#assert y is not x

num = 10.0
#assert isinstance(num, int)
assert isinstance(num, float)
assert isinstance(num, (int, float))

def custom_sum(*args):
    for v in args:
        if not isinstance(v, (int, float)):
            raise TypeError(f"custom_sum does not support type {type(v)} in arguments")
    s = 0
    for v in args:
        s += v
    return s

if custom_sum(1, 2, 3, 4, 5) != 15:
    print("should be 15")

assert custom_sum(1, 2, 3, 4, 5) == 15, "should be 15"
assert custom_sum() == 0, "should be 0"

def test_custom_sum():
    assert custom_sum(1, 2, 3, 4, 5) == 15, "should be 15"
    assert custom_sum() == 0, "should be 0"
    assert custom_sum(0) == 0, "should be 0"
    assert custom_sum(1, -1) == 0, "should be 0"

test_custom_sum()

class TestOrdinaryList(unittest.TestCase):
    def test_custom_sum(self):
        self.assertEqual(custom_sum(1, 2, 3, 4), 10, "should be 10")

class TestEmptyList(unittest.TestCase):
    def test_custom_sum(self):
        self.assertEqual(custom_sum(), 0, "should be 0")

class TestListOfZeros(unittest.TestCase):
    def test_custom_sum(self):
        self.assertEqual(custom_sum(0, 0, 0), 0, "should be 0")

class TestListWithNegatives(unittest.TestCase):
    def test_custom_sum(self):
        self.assertEqual(custom_sum(-1, -2, 2, 3), 2, "should be 2")

class TestAlwaysFAIL(unittest.TestCase):
    def test_custom_sum(self):
        self.assertEqual(custom_sum(), 10, "should be 2")

custom_sum("abc", "bcda")
custom_sum(10, "abc", "bcda")

class TestListOfIncorrectArgs(unittest.TestCase):
    def test_custom_sum(self):
        with self.assertRaises(TypeError):
            custom_sum(1, "2", 3, "4")