class areRotations
{
    //Function to check if two strings are rotations of each other or not.
    public static boolean areRotations(String s1, String s2 )
    {
        String temp = s1 + s1;
        
        return temp.contains(s2);
         
    }

    public static void main(String[] args) {
        String s = "geeksforgeeks";
        String t = "forgeeksgeeks";

        System.out.println(areRotations(s,t));
    }
    
}
