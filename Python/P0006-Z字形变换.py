def convert(s:str, numRows:int) -> str:
  if numRows < 2:
    return s
  rowList = [''] * numRows
  row = 0
  numRows -= 1
  for c in s:
    rowList[row] += c
    if row == 0:
      flag = 1
    if row == numRows:
      flag = -1
    row += flag
  return ''.join(rowList)
  
print(convert('a', 2))