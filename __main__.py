from game import Maze
import sys
from constant import KEYCODE_DIRECTION
import readchar
from function import ft_getInputInt, ft_atoi

def get_maze_dimensions():
  argc = len(sys.argv)
  if argc > 1 and ft_atoi(sys.argv[1]) is not None:
    size_x = ft_atoi(sys.argv[1])
    size_y = ft_atoi(sys.argv[2]) if argc > 2 and ft_atoi(sys.argv[2]) is not None else size_x
  else:
    size_x = ft_getInputInt("Enter width of the Maze : ")
    size_y = ft_getInputInt("Enter height of the Maze : ")
  return size_x, size_y

def get_seed():
  return sys.argv[3] if len(sys.argv) > 3 else None

size_x, size_y = get_maze_dimensions()
seed = get_seed()
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
  