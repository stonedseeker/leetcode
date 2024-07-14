

#include <bits/stdc++.h>
using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {

    if (!l1)
      return l2;
    if (!l2)
      return l1;

    ListNode *dummy = new ListNode(0, nullptr);
    ListNode *res = dummy;

    while (l1 && l2) {
      if (l1->val <= l2->val) {
        dummy->next = l1;
        l1 = l1->next;
        dummy = dummy->next;
      } else {
        dummy->next = l2;
        l2 = l2->next;
        dummy = dummy->next;
      }
    }

    if (l1) {
      dummy->next = l1;
    }

    if (l2) {
      dummy->next = l2;
    }

    return res->next;
  }
};

int main() {
  ListNode *node1 = new ListNode(1, new ListNode(2, new ListNode(4, nullptr)));
  ListNode *node2 = new ListNode(1, new ListNode(3, new ListNode(4, nullptr)));

  ListNode *node3 = Solution().mergeTwoLists(node1, node2);

  while (node3) {
    cout << node3->val << endl;
    node3 = node3->next;
  }

  return 0;
}
