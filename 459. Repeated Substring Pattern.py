class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        for i in range(1,n//2+1):
            if n%i == 0:
                substring = s[:i]
                repetitions = n // i
                constructed_substring= substring * repetitions

                if constructed_substring == s:
                    return True
        return False
