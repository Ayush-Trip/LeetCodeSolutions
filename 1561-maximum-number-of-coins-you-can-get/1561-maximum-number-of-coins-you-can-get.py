class Solution:
    def maxCoins(self, piles):
        piles.sort()
        total = 0
        pair = len(piles) // 3
        for i in range(pair, len(piles), 2):
            total += piles[i]
        return total