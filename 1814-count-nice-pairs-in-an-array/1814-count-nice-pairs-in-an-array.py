class Solution:
    def countNicePairs(self, nums):
        arr = {}
        for i in nums:
            temp = i - self.reverse(i)
            if temp in arr:
                arr[temp] += 1
            else:
                arr[temp] = 1
        res = 0
        mod = 1000000007
        for i in arr.values():
            res = (res % mod + (i * (i - 1) // 2)) % mod

        return int(res)

    def reverse(self, arr):
        rev = 0
        while arr > 0:
            rev = rev * 10 + arr % 10
            arr //= 10
        return rev