class Solution {
    public int countStudents(int[] s, int[] sa) {
        int[] arr = {0,0};
        for (int i : s) arr[i]++;
        for(int k:sa){
            if(arr[k]==0) break;
            arr[k]--;
        }
        return arr[0]+arr[1];
    }
}