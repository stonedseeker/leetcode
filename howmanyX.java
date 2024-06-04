class howmanyX {

    public static void main(String[] args) {
        System.out.println(count(3, 19, 1));
    }

    public static int count(int L, int R, int X) {
        L = L + 1;
        int count = 0;

        do {
            String temp = String.valueOf(L);
            for (int i = 0; i < temp.length(); i++) {                 
            
                if (temp.charAt(i) - '0' == X) {
                    System.out.println("True "+ temp.charAt(i) +  " = " + X + " " + temp);
                    count++;
                }
                
            }       
            L++;
        } while (L < R);
        return count;
    }
}

// 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
//
