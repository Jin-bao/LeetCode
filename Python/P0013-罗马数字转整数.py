class Solution:
  def romanToInt(self, s: str) -> int:
    romanNum = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    arabicNum = 0

    idx = 0
    idxLen = len(s)-1
    while idx < idxLen:
      if romanNum[s[idx]] < romanNum[s[idx+1]]:
        arabicNum -= romanNum[s[idx]]
      else:
        arabicNum += romanNum[s[idx]]
      
      idx += 1
    arabicNum += romanNum[s[idx]]

    return arabicNum

sln = Solution()
print(sln.romanToInt('MCMXCIV'))