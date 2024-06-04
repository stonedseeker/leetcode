class linkedCycleII {
    static class ListNode {
        int val;
        ListNode next; 

        private ListNode (int val) {
            this.val = val;
            this.next = null;
        }
    }

    public static void main(String[] args) {
        ListNode a = new ListNode(3);
        ListNode b = new ListNode(2);
        ListNode c = new ListNode(0);
        ListNode d = new ListNode(-4);

        a.next = b;
        b.next = c;
        c.next = d;
        d.next = b;

        ListNode one = new ListNode(1);
        ListNode two = new ListNode(2);

        one.next = two;
        two.next = one;



        ListNode ans = detectCycle(a);

        System.out.println(ans.val);
    }

    public static ListNode detectCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast.next != null && fast != null) {
            fast = fast.next.next;
            slow = slow.next;

            if (slow == fast){
                break;
            }
        }

        int lengthCycle = 0;

        do {
            slow = slow.next;
            lengthCycle++;
        } while (slow != fast);

        System.out.println(lengthCycle);

        //ListNode curr = head;

        while (lengthCycle != 0) {
            slow = slow.next;
            lengthCycle--;
        }

    
        return slow;
    } 

    
}
