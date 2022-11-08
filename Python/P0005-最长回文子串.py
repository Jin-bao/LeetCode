def lonPalStr(string:str) -> str:
  lPS = ''
  stringLen = len(string)
  for i in range(0, stringLen):
    for j in range(i+1, stringLen+1):
      subStr = string[i:j]
      if subStr==subStr[::-1] and len(subStr)>len(lPS):
        lPS = subStr
  return lPS

print(lonPalStr('cbbd'))