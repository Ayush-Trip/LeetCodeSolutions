class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i ,values in enumerate (nums):
            x=target-values
            if x in dic:
                return [i,dic[x]]
            else:
                dic[values]=i