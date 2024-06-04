
  // Definition for singly-linked list.


class ReOrderLinkedList {
    public static void main(String[] args) {
        ListNode one = new ListNode(1);
        ListNode two = new ListNode(2);
        ListNode three = new ListNode(3);
        ListNode four = new ListNode(4);

        one.next = two; 
        two.next = three;
        three.next = four;

        reorderList(one);
        
    }

    public static void reorderList(ListNode head) {
        if (head == null || head.next == null) return ; 

        ListNode fast = head; 
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            // System.out.println("Fast = " + fast.val);
            System.out.println("Slow = " + slow.val);
        }

        ListNode tail = null;

        while (slow != null) {
            ListNode temp = slow.next;
            slow.next = tail;
            tail = slow;
            slow = temp;
        }

        ListNode first = head;
        ListNode second = tail;

        while (second.next != null) {
            ListNode temp1 = first.next;
            ListNode temp2 = second.next;

            first.next = second;
            second.next = temp1;

            first = temp1;
            second = temp2;
        }
        
       
        ListNode curr = head;

        while (curr != null){
            System.out.println(curr.val);
            curr = curr.next;
        }

    }

}






public class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
 



