def ft_atoi(value):
  """ function ft_atoi แปลงค่าเป็น int ถ้าเป็นไปได้

  Args:
      value (any): ค่าที่จะแปลง

  Returns:
      int, none: ค่า int ถ้าเป็นไปได้ และ None ถ้าไม่เป็นไปได้
  """
  newVal = str(value).strip().lower()
  if newVal.isdigit() and int(newVal) > 1:
    return int(newVal)
  else:
    return None

def ft_getInputInt(prompt, loop = True):
  """ function ft_getInputInt รับค่าจากผู้ใช้และแปลงเป็น int

  Args:
      prompt (str): ข้อความที่จะแสดงให้ผู้ใช้
      loop (bool, optional): ให้ function นี้ loop หรือไม่ (สำหรับการ Test ต้องใส่ False ไม่งั้นจะเกิด loop). Defaults to True.

  Returns:
      int, none: ค่า int ถ้าเป็นไปได้ และ None ถ้าไม่เป็นไปได้
  """
  while True:
    tmp_input = ft_atoi(input(prompt))
    if tmp_input is None:
      print("Please enter a valid number")
      if not loop:
        return None
    else:
      return int(tmp_input)