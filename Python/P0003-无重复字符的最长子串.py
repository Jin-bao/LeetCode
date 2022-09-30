class LSSL:
  def longestSubStringLen(self, string:str) -> int:
    subString = []
    maxSubStrLen = 0
    for s in string:
      if s not in subString:
        subString += [s]
      else:
        if (subStrLen:=len(subString)) > maxSubStrLen:
          maxSubStrLen = subStrLen
        del subString[0:subString.index(s)+1]
        subString += [s]
    if (subStrLen:=len(subString)) > maxSubStrLen:
      return subStrLen
    else:
      return maxSubStrLen

if __name__ == '__main__':
  LSSL = LSSL()
  print(LSSL.longestSubStringLen('pwwkew'))