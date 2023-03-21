class Solution:
  def longestCommonPrefix(self, strs: list[str]) -> str:
    if not strs:
      return ""
    strs.sort()
    prefix = strs[0]
    for i in range(1, len(strs)):
      common = ""
      for j in range(min(len(prefix), len(strs[i]))):
        if prefix[j] == strs[i][j]:
          common += prefix[j]
        else:
          break    
      prefix = common
      if not prefix:
        return ""
    return prefix