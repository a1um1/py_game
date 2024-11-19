from game import Maze
import sys
from constant import KEYCODE_DIRECTION, PLAYER_CELL, EXIT_CELL, RESET
import readchar
from function import ft_getInputInt, ft_atoi

argc = len(sys.argv)
if (argc > 1 and ft_atoi(sys.argv[1]) is not None):
  size_x = ft_atoi(sys.argv[1])
  if (argc > 2 and ft_atoi(sys.argv[2]) is not None):
    size_y = ft_atoi(sys.argv[2])
  else:
    size_y = size_x
else:
  size_x = ft_getInputInt("Enter width of the Maze : ")
  size_y = ft_getInputInt("Enter height of the Maze : ")

seed = None
if len(sys.argv) > 3:
  seed = sys.argv[3]
maze = Maze(size_y, size_x, seed)
maze.ft_generate()
while True:
  maze.ft_display()
  while True:
    key = str(readchar.readkey()).lower()
    if key in KEYCODE_DIRECTION:
      if maze.ft_moveplayer(KEYCODE_DIRECTION[key]):
        exit(0)
      break
    elif key == 'q':
      print("\n You quit the game")
      exit(0)
  