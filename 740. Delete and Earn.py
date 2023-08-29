class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        f=[0]*(max(nums)+1)
        for i in nums:
            f[i]+=i
        dp=[0]*len(f)
        dp[1]=f[1]
        for i in range(2,len(f)):
            dp[i]=max(f[i]+dp[i-2],dp[i-1])
        return dp[len(f)-1]