class Solution {
    public List<String> buildArray(int[] target, int n) {
        var ans = new ArrayList<String>();
        int i = 0;
        for ( int j = 1; j <= target[target.length - 1] ; j++){
            ans.add("Push");
            if(j != target[i]){
                ans.add("Pop");
            }
            else{
                i++;
            }
        }
        return ans;
    }
}