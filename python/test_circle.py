import unittest
from math import pi
from circle import circleArea

class TestCircleModule(unittest.TestCase):
  def test_circleArea(self):
    self.assertAlmostEqual(circleArea(1), pi)
    self.assertAlmostEqual(circleArea(0), 0)
    self.assertAlmostEqual(circleArea(2.1), pi * 2.1**2)

  def test_values(self):
    self.assertRaises(ValueError, circleArea, -2)

  def test_types(self):
    self.assertRaises(TypeError, circleArea, True)
    self.assertRaises(TypeError, circleArea, "coucou")


