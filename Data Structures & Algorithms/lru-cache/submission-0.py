class LRUCache:
    class Node:
        def __init__(self, x: int, k: int, next: 'Node' = None, prev: 'Node' = None):
            self.val = int(x)
            self.key = int(k)
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.size = capacity
        self.key_to_node = {}
        self.left = self.Node(0, 0, None, None)
        self.right = self.Node(0, 0, None, None)
        self.left.next = self.right  # start empty: left ⇄ right
        self.right.prev = self.left
        self.curr_size = 0
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = self.Node(value, key, None, None)
            self.insert(node)
            self.key_to_node[key] = node
            self.curr_size += 1
            if self.curr_size > self.size:
                lru = self.left.next
                self.remove(lru)
                del self.key_to_node[lru.key]
                self.curr_size -= 1
            
            
            

        
        
