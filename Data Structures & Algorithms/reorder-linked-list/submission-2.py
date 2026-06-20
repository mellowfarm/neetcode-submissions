# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # separate into 2 linked lists
        curr_1 = head 
        length = 0
        while curr_1 is not None:
            length += 1
            curr_1 = curr_1.next
        
        mid = math.ceil(length/2)
        idx = 0
        end_1 = None
        head_2 = head # head of second list
        while idx < mid:
            end_1 = head_2
            head_2 = head_2.next
            idx += 1
        
        end_1.next = None 

        # reverse second list:
        curr_2_prev = None
        curr_2 = head_2
        if head_2 is None:
            return
        curr_2_next = curr_2.next
        while curr_2_next is not None:
            curr_2.next = curr_2_prev
            curr_2_prev = curr_2
            curr_2 = curr_2_next
            curr_2_next = curr_2_next.next
        curr_2.next = curr_2_prev

        # start reordering
        head_1 = head
        head_2 = curr_2

        while head_2 is not None:
            head_1_next = head_1.next    
            head_2_next = head_2.next

            head_1.next = head_2
            head_2.next = head_1_next

            head_1 = head_1_next
            head_2 = head_2_next
    

        
        

        