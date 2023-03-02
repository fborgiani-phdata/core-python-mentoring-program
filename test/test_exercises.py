from unittest import TestCase

from src.exercises import *


class Test(TestCase):
    def test_flip_array(self):
        # arrange
        expected = [3, 2, 1]
        test_input = [1, 2, 3]
        # act
        actual = flip_array(test_input)
        # assert
        self.assertEqual(expected, actual)

    def test_count_evens(self):
        # arrange
        expected = 3
        test_input = [2, 1, 2, 3, 4]
        # act
        actual = count_evens(test_input)
        # assert
        self.assertEqual(expected, actual)

    def test_generate_fibonacci(self):
        # arrange
        expected = [0, 1, 1, 2, 3, 5, 8]
        test_input = 6
        # act
        actual = generate_fibonacci(test_input)
        # assert
        self.assertEqual(expected, actual)

    def test_array_deduplication(self):
        # arrange
        expected = [8, 13, 9, 11, 12]
        test_input = [8, 13, 13, 9, 11, 12]
        # act
        actual = array_deduplication(test_input)
        # assert
        self.assertEqual(expected, actual)

    def test_array_sort(self):
        # arrange
        expected = [1, 2, 3, 4, 5]
        test_input = [5, 1, 4, 2, 3]
        # act
        actual = array_sort(test_input)
        # assert
        self.assertEqual(expected, actual)

    def test_array_intersection(self):
        # arrange
        expected = [1, 5]
        test_input_a = [1, 3, 5]
        test_input_b = [1, 5, 7]
        # act
        actual = array_intersection(test_input_a, test_input_b)
        # assert
        self.assertEqual(expected, actual)

        # arrange
        expected = [1]
        test_input_a = [1]
        test_input_b = [1, 5, 7]
        # act
        actual = array_intersection(test_input_a, test_input_b)
        # assert
        self.assertEqual(expected, actual)

        # arrange
        expected = [1]
        test_input_a = [1, 1, 1]
        test_input_b = [1, 5, 7]
        # act
        actual = array_intersection(test_input_a, test_input_b)
        # assert
        self.assertEqual(expected, actual)

        # arrange
        expected = []
        test_input_a = []
        test_input_b = []
        # act
        actual = array_intersection(test_input_a, test_input_b)
        # assert
        self.assertEqual(expected, actual)

    def test_int_to_roman(self):
        # arrange
        expected = "I"
        test_input = 1
        # act
        actual = int_to_roman(test_input)
        # assert
        self.assertEqual(expected, actual)

        # arrange
        expected = "III"
        test_input = 3
        # act
        actual = int_to_roman(test_input)
        # assert
        self.assertEqual(expected, actual)

        # arrange
        expected = "IV"
        test_input = 4
        # act
        actual = int_to_roman(test_input)
        # assert
        self.assertEqual(expected, actual)

        # arrange
        expected = "V"
        test_input = 5
        # act
        actual = int_to_roman(test_input)
        # assert
        self.assertEqual(expected, actual)

    def test_roman_to_int(self):
        # arrange
        expected = 1
        test_input = "I"
        # act
        actual = roman_to_int(test_input)
        # assert
        self.assertEqual(expected, actual)

        # arrange
        expected = 3
        test_input = "III"
        # act
        actual = roman_to_int(test_input)
        # assert
        self.assertEqual(expected, actual)

        # arrange
        expected = 4
        test_input = "IV"
        # act
        actual = roman_to_int(test_input)
        # assert
        self.assertEqual(expected, actual)

        # arrange
        expected = 3999
        test_input = "MMMCMXCIX"
        # act
        actual = roman_to_int(test_input)
        # assert
        self.assertEqual(expected, actual)

    def test_factorial_trailing_zeros(self):
        # arrange
        expected = 1
        test_input = 5
        # act
        actual = factorial_trailing_zeros(test_input)
        # assert
        self.assertEqual(expected, actual)

        # arrange
        expected = 4
        test_input = 20
        # act
        actual = factorial_trailing_zeros(test_input)
        # assert
        self.assertEqual(expected, actual)

    def test_two_sum(self):
        # arrange
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        # act
        actual = two_sum(nums, target)
        # assert
        self.assertEqual(expected, actual)

        # arrange
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        # act
        actual = two_sum(nums, target)
        # assert
        self.assertEqual(expected, actual)

        # arrange
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        # act
        actual = two_sum(nums, target)
        # assert
        self.assertEqual(expected, actual)

        # arrange
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        # act
        actual = two_sum(nums, target)
        # assert
        self.assertEqual(expected, actual)
