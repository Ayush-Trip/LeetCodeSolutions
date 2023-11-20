class Solution {
    public int maxFrequency(int[] nums, int k) {
        if (nums.length == 1){
            return 1;
        }
        Arrays.sort(nums);
        int l = 0;
        int maxf = 0;
        int op = 0;
        for(int i = 1; i< nums.length; i++){
            op = op + ((nums[i] - nums[i-1]) * (i-l));
            while(op > k){
                op -= nums[i] - nums[l];
                l += 1;
            }
            maxf = Math.max(maxf , i - l + 1);
        }
        return maxf;
    }
}