from constant import UP, DOWN, LEFT, RIGHT, MOVE_INSTRUCTION, OPPOSITE, WALL_CELL, EXIT_CELL, PLAYER_CELL, EMPTY_CELL, RESET
import random
import time
import os
class Maze:
  def __init__(self, rows, cols, seed = None):
    self.rows = rows
    self.cols = cols
    self.moveCount = 0
    self.grid = [
      [
        {
          'visited': False, 
          'walls': [True, True, True, True]
        } for _ in range(cols)
       ] for _ in range(rows)
    ]
    self.seed = seed
    if seed == None:
      self.seed = int(time.time())
    
    random.seed(self.seed)

    self.player = [
      random.randint(0, rows - 1),
      random.randint(0, cols - 1)
    ]
    self.exitPoint = [
      random.randint(0, rows - 1),
      random.randint(0, cols - 1)
    ]
  
  def ft_isinside(self, x, y):
    return 0 <= x < self.rows and 0 <= y < self.cols

  def ft_remove_wall(self, x, y, direction):
    self.grid[x][y]['walls'][direction] = False
    nx = x + MOVE_INSTRUCTION[direction][0]
    ny = y + MOVE_INSTRUCTION[direction][1]
    if self.ft_isinside(nx, ny):
      self.grid[nx][ny]['walls'][OPPOSITE[direction]] = False
  
  def ft_generate(self, x = 0, y = 0):
    self.grid[x][y]['visited'] = True
    directions = [UP, DOWN, LEFT, RIGHT]
    random.shuffle(directions)
    for direction in directions:
      nx = x + MOVE_INSTRUCTION[direction][0]
      ny = y + MOVE_INSTRUCTION[direction][1]
      if self.ft_isinside(nx, ny) and not self.grid[nx][ny]['visited']:
        self.ft_remove_wall(x, y, direction)
        self.ft_generate(nx, ny)
        
  def ft_display(self):
    line_buffer = []
    for x in list(range(self.rows)):
      line_buffer.append([WALL_CELL for _ in range(self.cols* 2)])
      line_buffer.append([WALL_CELL for _ in range(self.cols* 2)])
    for x in list(range(self.rows)):
      for y in list(range(self.cols)):
        (nx, ny) = (x * 2, y * 2)
        line_buffer[nx][ny] = "  "
        for direction in (RIGHT, LEFT, UP, DOWN):
          if not self.grid[x][y]['walls'][direction]:
            nx_offset, ny_offset = MOVE_INSTRUCTION[direction]
            line_buffer[nx + nx_offset][ny + ny_offset] = EMPTY_CELL
          
    line_buffer[self.exitPoint[0] * 2][self.exitPoint[1] * 2] = EXIT_CELL
    line_buffer[self.player[0] * 2][self.player[1] * 2] = PLAYER_CELL
    os.system('clear')
    print("Move count :", self.moveCount, PLAYER_CELL, "Player", RESET, EXIT_CELL, "Exit",RESET)
    print(WALL_CELL * ((self.cols * 2) + 1))
    for line in line_buffer:
      print(WALL_CELL, ''.join(line), sep='')
    print(RESET)
    print("Start playing by moving with ( W, A, S, D ) Or to quit press ( Q )")

  def ft_moveplayer(self, method):
    current_position = self.grid[self.player[0]][self.player[1]]
    if method in [UP, DOWN, LEFT, RIGHT]:
      if not current_position['walls'][method]:
        self.player[0] += MOVE_INSTRUCTION[method][0]
        self.player[1] += MOVE_INSTRUCTION[method][1]
        self.moveCount += 1
    return self.ft_check_is_win()
  
  def ft_check_is_win(self):
    (x,y) = self.player
    (nx,ny) = self.exitPoint
    if x == nx and y == ny:
      print("\n YOU WIN!!! 🥳 🎊 🎉")
      print(" You have completed the maze in", self.moveCount, "moves")
      print(" Seed used for this game:", self.seed)
      return True
    return False
    