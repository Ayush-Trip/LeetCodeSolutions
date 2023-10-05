class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cu = 0
        for i in nums:
            if cu == 0:
                c = i
                cu = 1
            elif i == c:
                cu += 1
            else:
                cu -= 1
        cu_c = nums.count(c)
        if cu_c > len(nums) // 2:
            return c