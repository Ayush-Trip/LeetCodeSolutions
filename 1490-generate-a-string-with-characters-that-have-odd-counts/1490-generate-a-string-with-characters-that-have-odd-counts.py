class Solution:
    def generateTheString(self, n: int) -> str:
        res = ""
        if n%2 != 0:
            return "a"*n
        res = "a"*(n-1)
        return res+"b"