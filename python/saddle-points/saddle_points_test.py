"""Tests for the saddle-points exercise

Implementation note:
The saddle_points function must validate the input matrix and raise a
ValueError with a meaningful error message if the matrix turns out to be
irregular.
"""
import unittest

from saddle_points import saddle_points


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class SaddlePointTest(unittest.TestCase):
    def test_identify_single_saddle_point(self):
        matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
        self.assertEqual(saddle_points(matrix), set([(1, 0)]))

    def test_empty_matrix_has_no_saddle_points(self):
        self.assertEqual(saddle_points([]), set())

    def test_identify_lack_of_saddle_points_when_there_are_none(self):
        matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
        self.assertEqual(saddle_points(matrix), set())

    def test_identify_multiple_saddle_points(self):
        matrix = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]
        expected = set([(0, 1), (1, 1), (2, 1)])
        self.assertEqual(saddle_points(matrix), expected)

    def test_identify_saddle_point_in_bottom_right_corner(self):
        matrix = [[8, 7, 9], [6, 7, 6], [3, 2, 5]]
        expected = set([(2, 2)])
        self.assertEqual(saddle_points(matrix), expected)

    # Additional tests for this track

    def test_irregular_matrix(self):
        matrix = [[3, 2, 1], [0, 1], [2, 1, 0]]
        with self.assertRaisesWithMessage(ValueError):
            saddle_points(matrix)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
