def myAtoi(s:str) -> int:
  NUM_MAX = 2**31-1
  NUM_MIN = -2**31
  nums = {'+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
  numStr = ''
  flag = 0
  for c in s:
    if c == ' ':
      if flag == 0:
        continue
      else:
        break
    else:
      if c in nums:
        if flag == 0:
          numStr += c
          flag = 1
        else:
          if c=='-' or c=='+':
            break
          else:
            numStr += c
        continue
      else:
        break
  try:
    num = int(numStr)
  except:
    return 0
  while num < NUM_MIN:
    num = NUM_MIN
  while num > NUM_MAX:
    num = NUM_MAX
  return num

print(myAtoi('+0 123'))