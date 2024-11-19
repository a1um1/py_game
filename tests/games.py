import unittest
import sys
import os
from unittest import mock

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
# https://www.geeksforgeeks.org/python-import-from-parent-directory/
# import from parent directory

from game import Maze
from constant import KEYCODE_DIRECTION
base_maze = Maze(5, 5, "test")
base_maze.ft_generate()
print("Base maze")
base_maze.ft_display()

class TestGameMethod(unittest.TestCase):

    def test_game_seed_same(self):
      maze_clone = Maze(5, 5, "test")
      maze_clone.ft_generate()
      self.assertEqual(base_maze.grid, maze_clone.grid) # Check if 2 maze are the same

    def test_game_seed_not_same(self):
      maze_clone = Maze(5, 5, "test_not_same")
      maze_clone.ft_generate()
      self.assertNotEqual(base_maze.grid, maze_clone.grid) # Check if 2 maze are the same
    
    def test_game_move_player(self):
      maze_clone = Maze(5, 5, "test")
      maze_clone.ft_generate()
      start_pos = base_maze.player

      maze_clone.ft_moveplayer(KEYCODE_DIRECTION['s'])
      self.assertEqual(maze_clone.player, start_pos)
      maze_clone.ft_moveplayer(KEYCODE_DIRECTION['d'])
      self.assertEqual(maze_clone.player, start_pos)

      maze_clone.ft_moveplayer(KEYCODE_DIRECTION['w'])
      self.assertNotEqual(maze_clone.player, start_pos)

      maze_clone.ft_moveplayer(KEYCODE_DIRECTION['s'])
      maze_clone.ft_moveplayer(KEYCODE_DIRECTION['a'])
      self.assertNotEqual(maze_clone.player, start_pos)

    def test_game_win(self):
      maze_clone = Maze(5, 5, "test")
      maze_clone.ft_generate()
      maze_clone.player = maze_clone.exitPoint
      self.assertTrue(maze_clone.ft_check_is_win())

if __name__ == '__main__':
    unittest.main(verbosity=2)
