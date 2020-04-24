class Node(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        self.cache_capacity = capacity
        self.cache = {}

        self.head, self.tail = Node(), Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        node = self.cache.get(key)

        if node:
            self.delete(node)
            self.add_to_front(key, node.val)

            return node.val

        return -1
            
    def put(self, key, value):
        node = self.cache.get(key)

        if node:
            self.delete(node)
        elif len(self.cache) == self.cache_capacity:
            self.delete(self.tail.prev)

        self.add_to_front(key, value)
        
    def add_to_front(self, key, value):
        node = Node(key, value)

        self.cache[key] = node

        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node
    
    def delete(self, node):
        next_node = node.next
        prev_node = node.prev

        next_node.prev, prev_node.next = prev_node, next_node

        self.cache.pop(node.key)
