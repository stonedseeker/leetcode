class ModTwo {
    public static void main(String[] args) {
        //832.575 812.025
        
        System.out.println(floatMod(832.575, 812.025));
    }

    public static Double floatMod(Double a, Double b) {
        System.out.println(Math.abs(a));
        System.out.println(Math.abs(b));
        System.out.println(Math.abs(a) % Math.abs(b));
        

         System.out.println(Math.abs(8333.57500000000000000068));

        System.out.println(20.550000000000068);
        System.out.println(Math.abs(20.550000000000068));
        Double ans = Math.abs(a) % Math.abs(b);
        return Math.abs(ans);




    }
}
