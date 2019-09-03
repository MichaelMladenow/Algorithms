import unittest
import sudoku


class TestSudokuHelpers(unittest.TestCase):
    def setUp(self):
        self.matrix = [  # 0 - means empty cell
            # 1  2  3  4  5  6  7  8  9
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],

            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],

            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

    def test_get_quadrant1(self):
        expected_quad = [
            [5, 3, 0],
            [6, 0, 0],
            [0, 9, 8]
        ]
        actual_quad = sudoku.get_quadrant(self.matrix, 0, 0)
        self.assertEqual(expected_quad, actual_quad,
                         "get_quadrant does not work.")

    def test_get_quadrant2(self):
        expected_quad = [
            [5, 3, 0],
            [6, 0, 0],
            [0, 9, 8]
        ]
        actual_quad = sudoku.get_quadrant(self.matrix, 1, 2)
        self.assertEqual(expected_quad, actual_quad,
                         "get_quadrant does not work.")

    def test_get_quadrant3(self):
        expected_quad = [
            [0, 0, 3],
            [0, 0, 1],
            [0, 0, 6]
        ]
        actual_quad = sudoku.get_quadrant(self.matrix, 4, 8)
        self.assertEqual(expected_quad, actual_quad,
                         "get_quadrant does not work.")

    def test_get_quadrant4(self):
        expected_quad = [
            [0, 0, 0],
            [4, 1, 9],
            [0, 8, 0]
        ]
        actual_quad = sudoku.get_quadrant(self.matrix, 8, 5)
        self.assertEqual(expected_quad, actual_quad,
                         "get_quadrant does not work.")


if __name__ == '__main__':
    unittest.main()