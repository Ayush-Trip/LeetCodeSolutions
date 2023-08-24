class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        count = 0
        ans = set()
        left = 0
        
        for i in range(n):
            if s[i] not in ans:
                ans.add(s[i])
                count = max(count, i - left + 1)
            else:
                while s[i] in ans:
                    ans.remove(s[left])
                    left += 1
                ans.add(s[i])
        
        return count
        