class Solution:
  def isFlipedString(self, str1:str, str2:str) -> bool:
    return len(str1)==len(str2) and str2 in str1+str1

StrRotation = Solution()
print(StrRotation.isFlipedString('waterbottle', 'erbottlewat'))