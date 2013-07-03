import unittest

import vector


class VectorTestCase(unittest.TestCase):

    def test_move_forwards_0_degrees(self):
        data = [0, 0, 0, 0]
        vector.move(data, 1)
        self.assertAlmostEqual(data[0], 1.0)
        self.assertAlmostEqual(data[1], 0.0)

    def test_move_backwards_0_degrees(self):
        data = [0, 0, 0, 0]
        vector.move(data, -1)
        self.assertAlmostEqual(data[0], -1.0)
        self.assertAlmostEqual(data[1], 0.0)

    def test_move_forwards_90_degrees(self):
        data = [0, 0, 90, 0]
        vector.move(data, 1)
        self.assertAlmostEqual(data[0], 0.0)
        self.assertAlmostEqual(data[1], 1.0)

    def test_move_backwards_90_degrees(self):
        data = [0, 0, 90, 0]
        vector.move(data, -1)
        self.assertAlmostEqual(data[0], 0.0)
        self.assertAlmostEqual(data[1], -1.0)

    def test_move_forwards_45_degrees(self):
        data = [0, 0, 45, 0]
        vector.move(data, 1)
        self.assertAlmostEqual(data[0], 0.7071067811)
        self.assertAlmostEqual(data[1], 0.7071067811)

    def test_move_backwards_45_degrees(self):
        data = [0, 0, 45, 0]
        vector.move(data, -1)
        self.assertAlmostEqual(data[0], -0.7071067811)
        self.assertAlmostEqual(data[1], -0.7071067811)

