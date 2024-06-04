class reorderLinkedList {
    public static void main(String[] args) {
        ListNode one = new ListNode(1);
        ListNode two = new ListNode(2);
        ListNode thr = new ListNode(3);
        ListNode four = new ListNode(4);

        one.next = two;
        two.next = thr;
        thr.next = four;

    }

    public static void reorderList(ListNode head) {

    }

}

public class ListNode () {
    private int val;
    private ListNode next;

    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) {this.val = val; this.next = next; }

}
