# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # find the number first
        curr1 = l1
        curr2 = l2
        number_sum1 = 0
        number_sum2 = 0
        power1 = 0
        power2 = 0
        while curr1 is not None:
            number_sum1 += curr1.val * (10**power1)
            power1 += 1
            curr1 = curr1.next
            
        while curr2 is not None:
            number_sum2 += curr2.val * (10**power2)
            power2 += 1
            curr2 = curr2.next

        digits = [int(digit) for digit in str(number_sum1 + number_sum2)]
        digits.reverse()

        res_head = None
        res_curr = None
        for digit in digits:
            if res_head is None:
                res_head = ListNode(digit, None)
                res_curr = res_head
            else:
                res_curr.next = ListNode(digit, None)
                res_curr = res_curr.next
        
        return res_head

        


