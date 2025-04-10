import unittest
from maze import Maze

# test cases
class Tests(unittest.TestCase):

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_different_sizes_1(self):
        num_cols = 5
        num_rows = 5
        m2 = Maze(0, 0, num_rows, num_cols, 15, 15)
        self.assertEqual(len(m2._cells), num_cols)
        self.assertEqual(len(m2._cells[0]), num_rows)

    def test_maze_different_sizes_2(self):
        num_cols = 3
        num_rows = 7
        m3 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(len(m3._cells), num_cols)
        self.assertEqual(len(m3._cells[0]), num_rows)

    def test_maze_zero_size(self):
        m4 = Maze(0, 0, 0, 0, 10, 10)
        self.assertEqual(len(m4._cells), 0)

if __name__ == "__main__":
    unittest.main()
