class Solution:
    def minDeletions(self, s: str) -> int:
        d={}
        res=0
        v=[]

        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        d=dict(sorted(d.items(),key=lambda x: x[1]))
        for i in d:
            if d[i] not in v:
                v.append(d[i])
            else:
                while d[i]!=0:
                    if d[i] not in v:
                        v.append(d[i])
                        break
                    d[i]=d[i]-1
                    res+=1
        return res