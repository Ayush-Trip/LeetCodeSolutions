class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        time=1
        ans=0
        if satisfaction[-1]<0:
            return ans
        total=0
        idx=0
        for i in range(len(satisfaction)-1,-1,-1):
            total+=satisfaction[i]
            idx=i
            if total<=0:
                idx+=1
                break
        for i in range (idx,len(satisfaction)):
            ans+=time*satisfaction[i]
            time+=1
        return ans