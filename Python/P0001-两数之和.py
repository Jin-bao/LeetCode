class Solution:
  def twoSum(self, nums:list[int], target:int) -> list[int]:
    hashmap={}
    for i,num in enumerate(nums):
      if hashmap.get(target-num) is not None:
        return [i, hashmap.get(target-num)]
      hashmap[num] = i

print(Solution().twoSum([3,2,4], 6))