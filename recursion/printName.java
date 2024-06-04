class printName {
    public static void main(String[] args) {
        String name = "Vaibhav Singh Chandel";
        pname(name, 5);
        // NtoOne(5);
        oneToNBackTrack(5);
    }

    public static void pname(String name, int n) {
        if (n == 0) {
            return;
        }

        System.out.println(name);
        pname(name, n-1);
    }

    public static void NtoOne(int N) {
        if (N == 0) return;

        System.out.println(N);
        NtoOne(N-1);
    }

    public static void oneToNBackTrack(int N){
        if (N == 0) return;

        oneToNBackTrack(N-1);
        System.out.println(N);
    }
}
