class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans=[]
        for i in words:
            temp=i.split(separator)
            for i in temp:
                if i!="":
                    ans.append(i)
        return ans