class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        o = 0 
        index = 0
        for i, j in enumerate(mat):
            c = j.count(1)
            if o < c:
                o = c
                index = i
        
        return [index,o]