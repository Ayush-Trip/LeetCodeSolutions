class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        for i in range(len(l)):
            v = nums[l[i]:r[i]+1]
            v.sort()
            temp = True
            if len(v) > 1:
                dif = v[1] - v[0]
                for j in range(1,len(v)) : 
                    if v[j] - v[j-1] != dif:
                        temp = False
                        break
            else:
                temp = False
            ans.append(temp)
        return ans
        