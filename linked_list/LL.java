public class LL {


    private Node head;
    private Node tail;
    private int size;
    
    public LL() {
        this.size = 0;
    }

    public void insertFirst(int value) {
        Node node = new Node(value);
        node.next = head;
        head = node;

        if (tail == null) {
            tail = head;
        } 

        size += 1;

    }

    public void displayList( ) {
        Node curr = head;
        while (curr != null){
            System.out.print(curr.value + " -> ");
            curr = curr.next;
        }
        System.out.println("END");
        System.out.println();
    }

    public void insertLast(int value) {
        if (tail == null) {
            insertFirst(value);
            return;
        }
        Node node = new Node(value);
        tail.next = node;
        tail = node;
        size++;
    }

    public void insertAt(int value, int index) {

        if (index == 0) {
            insertFirst(value);
            return;
        }
        
        Node temp = head; 

        for (int i = 1; i < index; i++) {
            temp = temp.next;
        }

        Node node = new Node(value, temp.next);
        
        temp.next = node; 
        size++;
    }

    public void insertRec(int val, int index) {
        head = insertRec(val, index, head);

    }

    private Node insertRec(int val, int index, Node node) {
        if (index == 0) {
            Node temp = new Node(val, node);
            size++;
            return temp;
        }

        node.next =  insertRec(val, --index, node.next);
        return node;
    }


    public void deleteFirst() {
        head = head.next;
    }

    private class Node {

        private int value;
        private Node next;

        public Node(int value) {
            this.value = value;
        }

        public Node(int value, Node next) {
            this.value = value;
            this.next = next;
        }
    }
    
} 
