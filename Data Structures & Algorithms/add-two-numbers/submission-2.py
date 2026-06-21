# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        res_curr = dummy
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            total = v1 + v2 + carry
            carry, digit = divmod(total, 10)
            res_curr.next = ListNode(digit, None)
            res_curr = res_curr.next
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
        if carry > 0:
            res_curr.next = ListNode(carry, None)
        
        return dummy.next


        


