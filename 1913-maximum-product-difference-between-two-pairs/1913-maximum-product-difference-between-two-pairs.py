class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums=sorted(nums)
        n=len(nums)-1
        return abs((nums[0]*nums[1])-(nums[n]*nums[n-1]))