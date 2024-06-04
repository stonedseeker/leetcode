import java.util.ArrayList;

class StringSubequences {
    public static void main(String[] args) {
        System.out.println(recurList("", "abc"));

        ArrayList<Integer> up = new ArrayList<>();
        up.add(1);
        up.add(2);

        up.add(5);

        // System.out.println(recInt(new ArrayList<Integer>(), up));
        ArrayList<Integer> p = new ArrayList<>();
        recInt(p, up);

    }

    public static void subsecs(String p, String up) {
        if (up.isEmpty()) {
            System.out.println(p);
            return;
        }
        //
        // subsecs(p + up.charAt(0), up.substring(1));
        // subsecs(p, up.substring(1));
        

    }

    public static ArrayList<String> recurList(String p, String up) {
        if (up.isEmpty()) {
            ArrayList<String> list = new ArrayList<>();
            list.add(p);
            return list;
        }

        ArrayList<String> left = recurList(p + up.charAt(0), up.substring(1));
        ArrayList<String> right = recurList(p, up.substring(1));

        left.addAll(right);

        return left;

        
    }
    
    // public static void recInt(ArrayList<Integer> p, ArrayList<Integer> up) {
    //
    //     if (up.size() <= 0) {
    //         System.out.println(p);
    //         return;
    //     }
    //
    //     recInt(p.add(up.get(0)), up.remove(0));
    //     recInt(p.add(up.get(0)), up.remove(0));
    //
    // }

    public static void recInt(ArrayList<Integer> p, ArrayList<Integer> up) {
        if (up.isEmpty()) {
            System.out.println(p);
            return;
        }

        // Copy the ArrayLists to avoid modifying the original lists
        ArrayList<Integer> pCopy = new ArrayList<>(p);
        ArrayList<Integer> upCopy = new ArrayList<>(up);

        // Pick the first element of the unprocessed list and add it to the processed list
        pCopy.add(upCopy.remove(0));
        // Recur with the updated lists
        recInt(pCopy, upCopy);

        // Do not add the first element of the unprocessed list to the processed list
        recInt(new ArrayList<>(p), new ArrayList<>(up));
    }
}
