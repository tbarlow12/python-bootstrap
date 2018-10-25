from unittest import TestCase

from mock import patch

from example_package.adder import Adder


class ExampleTest2(TestCase):

    def test_example(self):
        self.assertEqual(6, Adder.plus_three(3))
        self.assertEqual(9, Adder.plus_three(6))

        self.assertEqual(10, Adder.sum(5, 5))
        self.assertEqual(20, Adder.sum(17, 3))

        self.assertNotEqual(6, Adder.plus_three(68))
        self.assertNotEqual(6, Adder.plus_three(32))

        self.assertNotEqual(10, Adder.sum(1, 2))
        self.assertNotEqual(12, Adder.sum(2, 4))

    @patch.object(Adder, 'plus_three', return_value=100)
    def test_mock(self, multiplier):
        self.assertEqual(100, Adder.plus_three(2))
        self.assertEqual(100, Adder.plus_three(200))

        self.assertEqual(4, Adder.sum(2, 2))
        self.assertEqual(8, Adder.sum(5, 3))
