class MergeList {
    public static void main(String[] args) {
        ListNode one = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));

        ListNode two = new ListNode(5, new ListNode(6, new ListNode(7, new ListNode(8))));

        mergeLists(one, two);
    }

    public static void mergeLists(ListNode hf, ListNode hs) {
        
        if (hf == null && hs == null) return;
        if (hf == null) return;
        if (hs == null) return ;

        ListNode first = hf;
        ListNode second = hs;

        while(first.next != null && second.next != null) {
            ListNode temp1 = first.next;
            ListNode temp2 = second.next;

            first.next = second;
            second.next = temp1;

            first = temp1;
            second = temp2;
        }

        ListNode cur = hf;
        while(cur.next != null) {
            System.out.println(cur.val);
            cur = cur.next;
        }



    }
}

public class ListNode {
    int val;
    ListNode next;

    ListNode () {}
    ListNode (int val) {this.val = val;}
    ListNode (int val, ListNode next) {this.val = val; this.next = next ;}
}
