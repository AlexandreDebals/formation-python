import unittest
from calc import double, triple

class TestCalcModule(unittest.TestCase):
  def test_double(self):
    self.assertEqual(double(6), 12)
    #self.assertEqual(double(6), 13)

  def test_triple(self):
    self.assertEqual(triple(6), 18)
    #self.assertEqual(triple(6), 19)