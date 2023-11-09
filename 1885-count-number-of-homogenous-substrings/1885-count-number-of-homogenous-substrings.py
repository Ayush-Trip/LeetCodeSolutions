class Solution:
    def countHomogenous(self, s: str) -> int:
        m = 10**9 + 7
        ans = 0
        l = s[0]
        ir = 1

        for i in s[1:]:
            if i == l:
                ir += 1
            else:
                ans += ir * (ir + 1) / 2
                ir = 1
                l = i
        ans += ir * (ir + 1) / 2
        
        return int(ans) % m