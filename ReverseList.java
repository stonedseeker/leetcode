class ReverseList {

  
  public static void main(String[] args) {
    ListNode node = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, null)))));
    ListNode curr = node;
   

    ListNode poll = reverseList(node);
    ListNode temp = poll;
    while (temp!=null) {
      System.out.println(temp.val);
      temp = temp.next;
    }
  }
  
  public static ListNode reverseList(ListNode head) {
    ListNode curr = head;

    ListNode tail = null;
    
    while (curr != null) {
      ListNode temp = curr.next;
      curr.next = tail;
      tail = curr;
      curr = temp;
    }

    return tail;
  }

}

class ListNode {
  int val; 
  ListNode next;
  ListNode(int val) {
    this.val = val;
  }
  ListNode(int val, ListNode next) {
    this.val = val;
    this.next = next;
  }
}
