# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Find middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        slow.next = None

        # Step 2: Reverse second_half
        prev = 0
        while second_half:
            next_node = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = next_node
        rev_second_half = prev


        # Step 3: Interlace
        first_half = head
        while rev_second_half:
            first_next = first_half.next
            rev_second_next = rev_second_half.next

            first_half.next = rev_second_half
            rev_second_half.next = first_next

            first_half = first_next
            rev_second_half = rev_second_next