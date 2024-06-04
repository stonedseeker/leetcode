import java.util.LinkedList;


class sortedListIntersection {
    public static void main(String[] args) {
        Node a = new Node(1);
        Node b = new Node(2);

        Node c = new Node(3);

        Node d = new Node(4);

        Node e = new Node(5);

        Node f = new Node(6);

        a.next = b;
        b.next = c;
        c.next = d;
        d.next = e;
        e.next = f;

        Node one = new Node(2);
        Node two = new Node(4);
        Node three = new Node(6);

        Node four = new Node(8);

        one.next = two;
        two.next = three;
        three.next = four;

        Node curr = findIntersection(a, one);
        while (curr != null) {
            System.out.println(curr.data);
            curr = curr.next;
        }
    }

    public static Node findIntersection(Node head1, Node head2) {
        Node node1 = head1;
        Node node2 = head2;
        
        Node dummy = new Node(0);
        Node ans = dummy;
        
        while (node1 != null && node2 != null) {
            if (node1.data == node2.data) {
                ans.next = new Node(node1.data);
                ans = ans.next;
                node1 = node1.next;
                node2 = node2.next;
            } else {
                if (node1.data < node2.data) {
                    node1 = node1.next;
                } else {
                    node2 = node2.next;
                }
                
            }
        } 
        
        return dummy.next;
    }

    static class Node {
        int data;
        Node next;

        public Node(int data) {
            this.data = data;
            this.next = null;
        }

                  
    }
}
