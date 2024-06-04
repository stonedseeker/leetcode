public class DLL{

    private static Node head;
    private Node tail;
    private int size;

    public DLL() {
        this.size = 0;
    }

    private class Node {

        private int val;
        private Node next;
        private Node prev;

        public Node(int val) {
            this.val = val;
        }

        public Node(int val, Node next, Node prev) {
            this.val = val;
            this.next = next;
            this.prev = prev;
        }
    }


    public void insertFirst(int val) {
        Node node = new Node(val);
        node.next = head;
        if(head!= null) {
            head.prev = node;
        }
        node.prev = null;
        head = node;
 
    }

    public static void display(){
        Node curr = head;

        while (curr != null) {
            System.out.print(curr.val + " -> ");
            curr = curr.next;
        }

        System.out.println("END");
    }

    public void displayReverse(){
        Node curr = head;

        while (curr.next != null) {
            curr = curr.next;
        }

        while (curr != null) {
            System.out.print(curr.val + " -> ");
            curr = curr.prev;
        }
        System.out.println("Start");
    }

    public void insertLast(int val) {
        Node curr = head;
        while (curr.next != null) {
            curr = curr.next;
        }
        Node node = new Node(val, null, curr);
        curr.next = node;

    }

    public Node reverseList() {
        Node curr = head;
        head.prev = null;

        while (curr.next != null) {
            curr = curr.next; 
        }    

        head = curr;

        while (curr != null) {
            Node temp = curr.prev;
            curr.prev = curr.next;
            curr.next = temp;
            curr = curr.prev;
        }

    

        return head; 
    }



    
}
