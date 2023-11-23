class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        ArrayList<Boolean> ans = new ArrayList <>();
        for (int i = 0; i < l.length; i++){
            int[] v = Arrays.copyOfRange(nums, l[i], r[i]+1);
            Arrays.sort(v);
            boolean temp = true;
            if (v.length > 1){
                int dif = v[1] - v[0];
                for (int j = 1; j < v.length; j++){
                    if(v[j] - v[j-1] != dif){
                        temp = false;
                        break;
                    }
                }
            }
            else{
                temp = false;
            }
            ans.add(temp);
        }
        return ans;
    }
}