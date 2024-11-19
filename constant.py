
UP, DOWN, LEFT, RIGHT = (0,1,2,3)

MOVE_INSTRUCTION = {
  UP: (-1, 0),
  DOWN: (1, 0),
  LEFT: (0, -1),
  RIGHT: (0, 1),
}

OPPOSITE = {
  UP: DOWN,
  DOWN: UP,
  LEFT: RIGHT,
  RIGHT: LEFT,
}

WALL_CELL = "\033[1;36m██"
PLAYER_CELL = "\033[1;32m██"
EXIT_CELL = "\x1b[31m██"
EMPTY_CELL = "\x1b[48;5;238m  "
RESET = "\x1b[0m"

KEYCODE_DIRECTION = {
  'w': UP,
  'a': LEFT,
  's': DOWN,
  'd': RIGHT
}