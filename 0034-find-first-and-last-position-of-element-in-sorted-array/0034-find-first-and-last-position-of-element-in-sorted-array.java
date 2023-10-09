class Solution {
    public int[] searchRange(int[] nums, int target) {
        int f=-1;
        int l=-1;
        for(int i=0 ; i<nums.length; i++){
            if(nums[i]==target){
                f=i;
                while(i<nums.length && nums[i]==target){
                    i++;
                }
                l = i-1;
                return new int[]{f,l};
            }
        }
        return new int[]{f,l};
    }
}