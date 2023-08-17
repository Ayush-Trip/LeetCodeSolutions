class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=sum(nums)
        def digitsum(n):
            ans=0
            while n!=0:
                i=n%10
                ans+=i
                n=n//10
            return ans
        res=0
        for i in nums:
            if i>9:
                res+=digitsum(i)
            else:
                res+=i
        return abs(s-res)
