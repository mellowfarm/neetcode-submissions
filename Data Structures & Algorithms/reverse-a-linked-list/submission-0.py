# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        curr_prev = None
        curr = head
        curr_next = head.next
        while curr_next is not None:
            curr.next = curr_prev
            curr_prev = curr
            curr = curr_next
            curr_next = curr_next.next
        curr.next = curr_prev
        
        return curr