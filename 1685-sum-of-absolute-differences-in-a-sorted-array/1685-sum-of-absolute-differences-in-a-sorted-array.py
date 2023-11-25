class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        total = sum(nums)
        left = 0
        right = total
        for i in range(n):
            ans[i] = i * nums[i] - left + right - (n -i) * nums[i]
            left += nums[i]
            right -= nums[i]
        return ans