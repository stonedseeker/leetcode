/*
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. 
Return the linked list sorted as well.
*/
//1 1 3 4 4

class RemoveDuplicatesFromSortedArray {

    public static void main(String args[]) {
    
        ListNode node1 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(3, new ListNode(3, new ListNode (4, new ListNode(4, null)))))));
        ListNode node2 = new ListNode(1, new ListNode(1, new ListNode(2, null)));
        ListNode node = new ListNode(1, new ListNode(1, new ListNode(2, new ListNode(2, null))));
            
        ListNode curr = node;
        while (curr != null) {
            System.out.print(curr.val + " -> ");
            curr=curr.next;
        }
        System.out.println();

        ListNode cur = deleteDuplicates(node);

        while (cur != null) {
            System.out.print(cur.val + " -> ");
            
            cur=cur.next;
        }



    }

    public static ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        if (head.val == head.next.val) {
            try {
                int rm = head.val;
                while(head.val == rm) {
                    head = head.next;
                    System.out.println(head.val);
                }
            } catch (NullPointerException e) {
                return null;
            }
        }

        System.out.println(head.val);

        ListNode curr = head;

        try {
            while (curr.next.next != null) {
                if (curr.next.val == curr.next.next.val) {
                    int temp = curr.next.val;
                    while (curr.next.val == temp) {
                        curr.next = curr.next.next;
                        System.out.println(curr.val);
                    }
                } else {
                    curr = curr.next;
                }
            }
        } catch (NullPointerException e) {
            curr = curr.next;
        }

        

        // ListNode cur = head;
        // while (curr.next.next != null) {
        //     if (curr.next.val == curr.next.next.val && curr.next.next.next == null) {
        //         curr.next = null;
        //     }
        // }

        return head;

    }
}

class ListNode {
    int val;
    ListNode next;

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
