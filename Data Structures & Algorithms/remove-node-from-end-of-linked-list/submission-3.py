# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
        
        idx = length - n
        curr_idx = 0
        prev_node = None
        curr_node = head
        while curr_idx != idx:
            curr_idx += 1
            prev_node = curr_node
            curr_node = curr_node.next
        
        if prev_node is None:
            head = curr_node.next
            return head
        
        prev_node.next = curr_node.next
        return head
