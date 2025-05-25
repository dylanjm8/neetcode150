class Node:
# Creating a doubly Linked list cache with given size (goes both ways)

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
# hashMap pointing to node 
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # mapping keys to nodes

        self.left, self.right = Node(0,0), Node(0,0)
        # left is least recent & right is most recent
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node): # we pass in a self.node, so doesn't have to be reffered to again by self
        # remove at left. essentially skipping the middle node
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        # inserting at right
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        # should return corresponding value for key, if null return -1
        if key in self.cache:
            # want to remove from list and reinsert it to simulate being new most recent cache entry
            self.remove(self.cache[key]) 
            self.insert(self.cache[key]) # . -> either a function or an instance variable 
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # add key-value, update key-value, evict LRU key-value if cache is full (using L R pointers)
        # R and L pointers created as dummy nodes
        if key in self.cache:
            self.remove(self.cache[key])
            
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from linked list AND delete from HM
            lru = self.left.next
            self.remove(lru) 
            del self.cache[lru.key]


