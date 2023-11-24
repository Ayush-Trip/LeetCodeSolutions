class Solution {
    public int maxCoins(int[] piles) {
        Arrays.sort(piles);
        int total = 0;
        int pair = piles.length / 3;
        for (int i = pair ; i < piles.length; i += 2){
            total += piles[i];
        }
        return total;
    }
}