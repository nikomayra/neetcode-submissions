"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
    
        # Step 1: Create copy nodes and interweave
        curr = head
        while curr:
            copy_node = Node(curr.val)
            copy_node.next = curr.next
            curr.next = copy_node
            curr = copy_node.next
        
        # Step 2: Set random pointers for copy nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Step 3: Separate the lists
        dummy = Node(0)
        copy_curr = dummy
        curr = head
        
        while curr:
            copy_curr.next = curr.next
            curr.next = curr.next.next
            copy_curr = copy_curr.next
            curr = curr.next
        
        return dummy.next

    