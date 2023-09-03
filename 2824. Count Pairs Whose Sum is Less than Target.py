class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        c=0
        for i in range (len(nums)):
            for j in range(len(nums)):
                if nums[i]+ nums[j] < target and 0<=i<j :
                    c+=1
        return c