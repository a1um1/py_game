def ft_atoi(value):
  newVal = str(value).strip().lower()
  if newVal.isdigit() and int(newVal) > 1:
    return int(newVal)
  else:
    return None

def ft_getInputInt(prompt, loop = True):
  while True:
    tmp_input = ft_atoi(input(prompt))
    if tmp_input is None:
      print("Please enter a valid number")
      if not loop:
        return None
    else:
      return int(tmp_input)