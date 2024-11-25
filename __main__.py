from game import Maze
import sys
from constant import KEYCODE_DIRECTION
import readchar

import sys
sys.setrecursionlimit(10**6)

from function import ft_getInputInt, ft_atoi

def ft_get_maze_dimensions():
  """ function ft_get_maze_dimensions รับค่าความกว้างและความสูงของวงกต

  Returns:
      (int, int): ความกว้างและความสูงของวงกต
  """
  argc = len(sys.argv)
  if argc > 1 and ft_atoi(sys.argv[1]) is not None:
    size_x = ft_atoi(sys.argv[1])
    size_y = ft_atoi(sys.argv[2]) if argc > 2 and ft_atoi(sys.argv[2]) is not None else size_x
  else:
    size_x = ft_getInputInt("Enter width of the Maze : ")
    size_y = ft_getInputInt("Enter height of the Maze : ")
  return size_x, size_y

def ft_get_seed():
  """
    function ft_get_seed รับค่า seed จาก command line
    Returns:
        any, none: ค่า seed ถ้ามี และ None ถ้าไม่มี
  """
  return sys.argv[3] if len(sys.argv) > 3 else None

size_x, size_y = ft_get_maze_dimensions()
seed = ft_get_seed()
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
  