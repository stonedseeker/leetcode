#include <iostream>
using namespace std;

//  * Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  void reorderList(ListNode *head) {
    if (head == NULL || head->next == NULL)
      return;

    // 1 2 3 4
    //
    ListNode *slow = head;
    ListNode *fast = head;

    while (fast != NULL && fast->next != NULL) {
      fast = fast->next->next;
      slow = slow->next;
      cout << "Fast => " << fast->val;
      cout << "Slow => " << slow->val;
    }

    ListNode *tail = NULL;

    // 1->2->3->4->5->6->7->8
    //             slow
    //
    // while (slow != NULL) {
    //   ListNode *temp = slow->next;
    // }
    //
    cout << "This is slow => " << slow->val;
    return;

    // ListNode *dummy = new ListNode(0);
    // dummy = head;
    // ListNode *curr = dummy;
    //
    // while (curr->next != NULL) {
    //   curr = curr->next;
    // }
    //
    // ListNode *temp = head->next;
    // head->next = curr;
    // curr->next = temp;
    // reorderList(temp->next);
    //
    // cout << "The head of the list = " << dummy->val;
  }
};

int main() {
  ListNode *one = new ListNode(1);
  ListNode *two = new ListNode(2);

  ListNode *three = new ListNode(3);

  ListNode *four = new ListNode(4);

  one->next = two;
  two->next = three;
  three->next = four;

  Solution().reorderList(one);
}
