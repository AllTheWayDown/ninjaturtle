import unittest

from ninjaturtle.ninja import NinjaTurtle
from ninjaturtle.common import DEFAULT_MAX_SPEED
from ninjaturtle.engine import get_engine


class NinjaTurtleTest(unittest.TestCase):

    def setUp(self):
        super(NinjaTurtleTest, self).setUp()

    def tearDown(self):
        super(NinjaTurtleTest, self).tearDown()

    def test_max_speed_getter(self):
        turtle = NinjaTurtle(get_engine())
        self.assertAlmostEqual(turtle.max_speed(), DEFAULT_MAX_SPEED)

    def test_max_speed_setter(self):
        turtle = NinjaTurtle(get_engine())
        testValue = 999.0
        self.assertEqual(turtle.max_speed(testValue), None)
        self.assertAlmostEqual(turtle._max_speed, testValue)

if __name__ == '__main__':
    unittest.main()
