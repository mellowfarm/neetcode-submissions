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
        
        # push the heads into the heap first; i prevents node objects from being compared
        for i, l in enumerate(lists):
            if l is not None:
                heapq.heappush(heap, (l.val, i, l))

        while heap:
            val, i, node = heapq.heappop(heap)
            res.next = node
            res = res.next
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
