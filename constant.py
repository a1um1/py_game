
"""
  ไฟล์นี้เป็นไฟล์ที่ใช้เก็บค่าคงที่ที่ใช้ในโปรแกรม เช่น 
   - ค่าสีของ cell ต่าง ๆ
   - ค่าที่ใช้ในการเคลื่อนที่ของผู้เล่น
   - ค่าที่ใช้ในการเปลี่ยนทิศทางของผู้เล่น
   - ตัวอักษร ASCII ที่ใช้แสดงผล
   - ตัวอักษรที่ใช้ในการควบคุมการเคลื่อนที่ของผู้เล่น
"""

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

RESET = "\x1b[0m"
WALL_CELL = "\033[1;36m██"
PLAYER_CELL = "\033[1;32m██"
EXIT_CELL = "\x1b[31m██"
EMPTY_CELL = "  "

KEYCODE_DIRECTION = {
  'w': UP,
  'a': LEFT,
  's': DOWN,
  'd': RIGHT
}