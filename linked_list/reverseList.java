class reverseList {

    public static void main(String[] args) {
        
        ListNode a = new ListNode(1);
        ListNode b = new ListNode(2);
        ListNode c = new ListNode(3);
        ListNode d = new ListNode(4);
        ListNode e = new ListNode(5);
        ListNode f = new ListNode(6);
        ListNode g = new ListNode(7);
        ListNode h = new ListNode(8);



        
        a.next = b;
        b.next = c;
        c.next = d;
        d.next = e;
        e.next = f;
        f.next = g;
        g.next = h;

        ListNode ans = reverse(a);

        while (ans != null) {
            System.out.print(ans.val + " -> ");
            ans = ans.next;
        }
        System.out.println("end");

        ListNode ans1 = inPlaceReverse(a);

        while (ans1 != null) {
            System.out.print(ans1.val + " -> ");
            ans1 = ans1.next;
        }
        System.out.println("end");
    }


    public static ListNode reverse(ListNode head) {
        ListNode tail = null;

        while (head != null) {
            ListNode val = new ListNode(head.val);
            val.next = tail;
            tail = val;
            head = head.next;
        }

        return tail;
    }

    public static ListNode inPlaceReverse(ListNode head) {
        ListNode prev = null;
        ListNode present = head;
        ListNode next = present.next;

        while(present != null) {
            present.next = prev;
            prev = present;
            present = next;
            if (next != null) next = next.next;
        }

        return prev;
    }
    
}

class ListNode {
    int val;
    ListNode next;

    public ListNode(int val) {
        this.val = val;
        this.next = null;
    } 

}
