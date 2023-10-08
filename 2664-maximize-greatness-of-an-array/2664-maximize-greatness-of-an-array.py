class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        j=0
        for i in nums:
            if nums[j] < i:
                j+=1
        return j