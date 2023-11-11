class Solution {
    public int maxProduct(String[] words) {

        int n = words.length;
        Arrays.sort(words, (a,b) -> b.length() - a.length());
        int max = 0;

        for(int i = 0; i < n; i++){
            for(int j = i+1; j < n; j++){
                if(!hasCommonCharacters(words[i], words[j])){
                    max = Math.max(max, words[i].length() * words[j].length());

                    if(words[i].length() * words[j].length() <= max){
                        break;
                    }
                }
            }
        }
        return max;
    }


    private boolean hasCommonCharacters(String word1, String word2){
        int ch[] = new int[26];

        for(char c: word1.toCharArray()){
            ch[c-'a']++;
        }


        for(char c: word2.toCharArray()){
            if(ch[c-'a'] > 0){
                return true;
            }
        }
        return false;
    }
}

