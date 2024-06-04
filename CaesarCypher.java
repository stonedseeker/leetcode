class CaesarCypher {
    public static void main(String[] args) {
        String in = "All the best";
        System.out.println(caesarCypher(in, 1));;
    }

    public static String caesarCypher(String str, int key) {
        StringBuilder res = new StringBuilder();
        for (Character c : str.toCharArray()) {

            if (Character.isLetter(c)) {
                char base = Character.isUpperCase(c) ? 'A' : 'a';
                int offset = c - base;
                int shifted = (offset + key) % 26;
                res.append((char) (base + shifted));
            } else {
                res.append(c);
            }



        }

        return res.toString();
    } 
}
