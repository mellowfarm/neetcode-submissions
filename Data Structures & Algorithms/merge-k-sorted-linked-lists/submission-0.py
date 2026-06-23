# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        heap = []
        dummy = ListNode(0, None)
        res = dummy
        for list in lists:
            curr = list
            while curr is not None:
                heapq.heappush(heap, curr.val)
                curr = curr.next

        while heap:
            res.next = ListNode(heapq.heappop(heap), None)
            res = res.next
        
        return dummy.next
