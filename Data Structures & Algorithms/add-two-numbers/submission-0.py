# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        carry = 0
        prev = None
        
        # Process while either list has nodes or there's carry
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            if l1:  # Reuse existing l1 node
                l1.val = total % 10
                prev = l1
                l1 = l1.next
            else:  # Create new node when l1 is exhausted
                new_node = ListNode(total % 10)
                prev.next = new_node
                prev = new_node
            
            if l2:
                l2 = l2.next
            carry = total // 10
        
        return head