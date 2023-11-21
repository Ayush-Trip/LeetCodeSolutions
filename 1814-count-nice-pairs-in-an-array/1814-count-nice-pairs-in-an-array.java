import java.util.HashMap;
import java.util.Map;
class Solution {
    public int countNicePairs(int[] nums) {
        Map<Integer, Integer> arr = new HashMap<>();
        for (int i : nums) {
            int temp = i - reverse(i);
            arr.put(temp, arr.getOrDefault(temp, 0) + 1);
        }
        long res = 0;
        int mod = 1000000007;
        for (int i : arr.values()) {
            res = (res % mod + ((long) i * (i - 1) / 2) % mod) % mod;
        }
        return (int) res;
    }
    private int reverse(int num) {
        int rev = 0;
        while (num > 0) {
            rev = rev * 10 + num % 10;
            num /= 10;
        }
        return rev;
    }
}
