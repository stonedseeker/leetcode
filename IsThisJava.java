class IsThisJava {
    
    public static void multiline() {
        var Shakespeare = """ 

            To be, or not to be, that is the question:
            Whether 'tis nobler in the mind to suffer 
            The 
            """;

        System.out.println(Shakespeare);

    // Assertions.assertNotEquals(Shakespeare.charAt(0), 'T');
    // Shakespeare = Shakespeare.stripLeading();
    // Assertions.assertEquals(Shakespeare.charAt(0), 'T');
    }

    public static void main(String[] args) {
        multiline();
    }
}
