import unittest
from math import sin, cos, radians

from ninjaturtle import vector
from ninjaturtle.engine import TurtleModel


class VectorTestCase(unittest.TestCase):

    def setUp(self):
        super(VectorTestCase, self).setUp()
        self.data = TurtleModel.DEFAULT_TURTLE[:]

    def test_rotate_90(self):
        vector.rotate(self.data, 90)
        self.assertAlmostEqual(self.data[4], 90)
        self.assertAlmostEqual(self.data[6], cos(radians(90)))
        self.assertAlmostEqual(self.data[7], sin(radians(90)))

    def test_rotate_minus_90(self):
        vector.rotate(self.data, -90)
        self.assertAlmostEqual(self.data[4], -90)
        self.assertAlmostEqual(self.data[6], cos(radians(-90)))
        self.assertAlmostEqual(self.data[7], sin(radians(-90)))

    def test_move_forwards_0_degrees(self):
        vector.move(self.data, 1)
        self.assertAlmostEqual(self.data[0], 1.0)
        self.assertAlmostEqual(self.data[1], 0.0)

    def test_move_backwards_0_degrees(self):
        vector.move(self.data, -1)
        self.assertAlmostEqual(self.data[0], -1.0)
        self.assertAlmostEqual(self.data[1], 0.0)

    def test_move_forwards_90_degrees(self):
        vector.rotate(self.data, 90)
        vector.move(self.data, 1)
        self.assertAlmostEqual(self.data[0], 0.0)
        self.assertAlmostEqual(self.data[1], 1.0)

    def test_move_backwards_90_degrees(self):
        vector.rotate(self.data, 90)
        vector.move(self.data, -1)
        self.assertAlmostEqual(self.data[0], 0.0)
        self.assertAlmostEqual(self.data[1], -1.0)

    def test_move_forwards_45_degrees(self):
        vector.rotate(self.data, 45)
        vector.move(self.data, 1)
        self.assertAlmostEqual(self.data[0], 0.7071067811)
        self.assertAlmostEqual(self.data[1], 0.7071067811)

    def test_move_backwards_45_degrees(self):
        vector.rotate(self.data, 45)
        vector.move(self.data, -1)
        self.assertAlmostEqual(self.data[0], -0.7071067811)
        self.assertAlmostEqual(self.data[1], -0.7071067811)
