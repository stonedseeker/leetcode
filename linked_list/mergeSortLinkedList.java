class mergeSortLinkedList{
    static class ListNode {
        int val;
        ListNode next;

        private ListNode(int val) {
            this.val = val;
            this.next = null;
        }
    }


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

        ListNode curr = sortList(a);

        while (curr != null) {
            System.out.println(curr.val);
            curr = curr.next;
        }
    }

    public static ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode mid = getMidTwo(head);
        ListNode left = sortList(head);
        ListNode right = sortList(mid);

        return merge(left, right);
    }

    public static ListNode merge(ListNode l1, ListNode l2) {

        ListNode dummy = new ListNode(0);
        ListNode ans = dummy;

        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                ans.next = l1;
                ans = ans.next;
                l1 = l1.next;
            } else {
                    ans.next = l2;
                    ans = ans.next;
                    l2 = l2.next;
                } 
        }

        ans.next = (l1 != null) ? l1:l2;
        return dummy.next;
    }



    public static ListNode getMid(ListNode head) {
        ListNode midPrev = null;
        while (head != null && head.next != null) {
            midPrev = (midPrev == null) ? head : midPrev.next;
            head = head.next.next;
        }

        ListNode mid = midPrev.next;
        midPrev.next = null;
        return mid;
    }

     public static ListNode getMidTwo(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode curr = head;
        ListNode prev = null;

        while (curr != slow) {
            prev = curr;
            curr = curr.next;
        }

        if (prev != null) {
            prev.next = null; // Cut off the remaining part after slow
        }

        ListNode i = slow;

        while (i != null) {
            System.out.print(i.val + " -> ");
            i = i.next;
        }
        System.out.print("END");
        System.out.println();
        System.out.println("returned this");


        return slow;
     
     }
     



}
