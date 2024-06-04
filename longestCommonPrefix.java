class longestCommonPrefix {
    String longestCommonPrefix(String arr[], int n){
        String res = ""
        String minStr = arr[0];
        for (int i = 0, i < arr.length; i++) {
            if (arr[i].length < minStr) {
                minStr = arr[i];
            }
        }
        
        for (int i : arr) {
            for (int j = 0, k = 0; j < minStr.length(); i++) {
                char s = minStr.toCharArray();
            }
        }

        return res;
        
    }

    p
}
