class Solution {
    public int[] getSumAbsoluteDifferences(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n]; 
        int total =  Arrays.stream(nums).sum();
        int left = 0;
        int right =total;
        for (int i =0; i < n; i++){
            ans[i] = i * nums[i] - left + right - (n - i) * nums[i];
            left += nums[i];
            right -= nums[i];
        }
        return ans;
    }
}