from unittest import TestCase

from mock import patch

from example_package.multiplier import Multiplier


class ExampleTest(TestCase):

    def test_example(self):
        self.assertEqual(6, Multiplier.times_two(3))
        self.assertEqual(6, Multiplier.times_three(2))

        self.assertNotEqual(6, Multiplier.times_two(2))
        self.assertNotEqual(6, Multiplier.times_three(3))

    @patch.object(Multiplier, 'times_three', return_value=100)
    def test_mock(self, mock_object):
        self.assertEqual(100, Multiplier.times_three(2))
        self.assertEqual(100, Multiplier.times_three(200))

        self.assertEqual(4, Multiplier.times_two(2))
        self.assertEqual(8, Multiplier.times_two(4))
