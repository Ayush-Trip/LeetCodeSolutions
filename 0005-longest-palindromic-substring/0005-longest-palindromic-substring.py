class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for l in range(0,len(s)):
            for r in range(l+1+len(ans),len(s)+1):
                word = s[l:r]
                if word == word[::-1]:
                    ans = word
        return ans