class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        ans=[]
        while(i<len(firstList) and j<len(secondList)):
            first=firstList[i]
            second=secondList[j]
            if second[0]<=first[1] and second[1]>=first[0]:
                ans.append([max(first[0],second[0]),min(first[1],second[1])])
                if first[1]<second[1]:
                    i+=1
                else:
                    j+=1
            else:
                if first[1]<second[1]:
                    i+=1
                else:
                    j+=1
        return ans