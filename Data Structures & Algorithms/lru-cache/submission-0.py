class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # a given key in this map will point to a node in the doubly linked list

        # we need to maintain dummy nodes to refer to the head and the tail of the linked list
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        # when we remove a node, we remove it at the head of the list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        # when we insert a node, we insert it at the tail of the list
        tmp = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = tmp
        node.prev.next = node

    def get(self, key: int) -> int:
        # we remove the node from it's current position, insert it at the tail of the list and return it's value
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 # if key does not exist in the cache
        

    def put(self, key: int, value: int) -> None:
        # if key exists, we remove from it's current position and insert at tail, otherwise just insert at tail
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # if the cache length has exceeded the capacity we need to remove the node at the head of the list
        if len(self.cache) > self.capacity:
            # severe the current head from the list
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
