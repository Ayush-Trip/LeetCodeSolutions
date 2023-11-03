class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s=[]
        for i in range (1,target[-1]+1) :
            s.append("Push")
            if i not in target:
                print(i)
                s.append("Pop")
        
        return s