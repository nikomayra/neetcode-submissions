# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr = head

        while curr:
            if curr.val in visited:
                return True
            visited.add(curr.val)
            curr = curr.next
        return False