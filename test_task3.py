import unittest
import Sudoku


class SudokuTest(unittest.TestCase):
    def test_solution(self):

        # test 1
        self.assertEqual(Sudoku.check_sudoku("..\\sudoku_right"), True)

        # test 2
        self.assertEqual(Sudoku.check_sudoku("..\\sudoku_wrong"), False)


if __name__ == '__main__':
    unittest.main()
