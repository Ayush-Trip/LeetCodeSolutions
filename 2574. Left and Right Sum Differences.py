class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ls=[0]
        rs=[0]
        ans=[]
        for i in range(n-1):
            ls.append(nums[i]+ls[-1])
        for j in range(n-1,0,-1):
            rs.append(nums[j]+rs[-1])
        rs.reverse()
        for i in range(n):
            ans.append(abs(ls[i]-rs[i]))
        return ans