class LRUCache:

    class Node:
        def __init__(self, key: int, val: int, nxt: "Node", prev: "Node"):
            self.key = int(key)
            self.val = int(val)
            self.nxt = nxt
            self.prev = prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_size = 0
        self.key_to_node = {}
        self.front_cache = self.Node(0, 0, None, None) # points to LRU
        self.back_cache = self.Node(0, 0, None, None) # append new nodes/just used
        self.front_cache.nxt = self.back_cache
        self.back_cache.prev = self.front_cache

    def insert(self, node):
        curr_last = self.back_cache.prev
        node.prev = curr_last
        node.nxt = self.back_cache
        curr_last.nxt = node
        self.back_cache.prev = node
    
    def delete(self, node):
        node.nxt.prev = node.prev
        node.prev.nxt = node.nxt
    
    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.delete(node)
            self.insert(node)
            return self.key_to_node[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.delete(node)
            self.insert(node)
        else:
            node = self.Node(key, value, None, None)
            self.insert(node)
            self.key_to_node[key] = node
            self.curr_size += 1
            if self.curr_size > self.capacity:
                lru = self.front_cache.nxt
                self.delete(lru) # evict
                del self.key_to_node[lru.key]
                self.curr_size -= 1  
