from linkedlistpalindrome import Solution, ListNode

# Create a linked list
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node2.next = node3
node1.next = node2

# Create an instance of the Solution class
solution = Solution()

# Test the isPalindrome method
result = solution.isPalindrome(node1)
print(result)

# Exit Python
exit()

