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
        # deep copy the values first
        curr = head 
        copy_head = None
        copy_curr = None
        node_to_random = {}
        og_to_copy = {}
        while curr is not None:
            curr_val = curr.val
            curr_random = curr.random
            if copy_head is None:
                copy_head = Node(curr_val, None, None)
                copy_curr = copy_head
            else:
                copy_curr.next = Node(curr_val, None, None)
                copy_curr = copy_curr.next
            node_to_random[copy_curr] = curr_random
            og_to_copy[curr] = copy_curr
            curr = curr.next

        # deep copy the random
        for node, random in node_to_random.items():
            if random is None:
                node.random = None
            else:
                node.random = og_to_copy[random]
        
        return copy_head