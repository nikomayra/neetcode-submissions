class Node:
    """
    A doubly-linked list node that stores a key-value pair.
    Each node knows about its previous and next neighbors.
    """
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None  # Points to the previous node in the list
        self.next = None  # Points to the next node in the list


class LRUCache:
    """
    LRU (Least Recently Used) Cache implementation using a hash map + doubly linked list.
    
    The doubly linked list maintains order by recency:
    - Most recently used items are near the RIGHT dummy node
    - Least recently used items are near the LEFT dummy node
    
    Structure: [HEAD] <-> [LRU item] <-> ... <-> [MRU item] <-> [TAIL]
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map: key -> Node (for O(1) access)
        
        # Create sentinel nodes to simplify edge cases
        # These act as boundaries - they never store real data
        # Using None/invalid values to distinguish from actual data
        self.head = Node(-1, -1)   # Sentinel at LRU end (key/value can't be negative)
        self.tail = Node(-1, -1)   # Sentinel at MRU end
        
        # Initially, sentinels point to each other (empty list)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_from_list(self, node):
        """
        Remove a node from the doubly linked list.
        
        Before: [A] <-> [node] <-> [B]
        After:  [A] <-> [B]
        
        The node still exists but is no longer connected to the list.
        """
        # Connect the node's neighbors to each other, bypassing this node
        node.prev.next = node.next  # A's next pointer now points to B
        node.next.prev = node.prev  # B's prev pointer now points to A

    def insert_at_mru_position(self, node):
        """
        Insert a node at the Most Recently Used position (right before tail sentinel).
        
        Before: [...] <-> [prev_mru] <-> [TAIL]
        After:  [...] <-> [prev_mru] <-> [node] <-> [TAIL]
        """
        # Find where to insert: between the current MRU item and tail
        prev_mru = self.tail.prev  # The current most recently used item
        next_pos = self.tail       # The tail sentinel (always at the end)
        
        # Connect the previous MRU item to our new node
        prev_mru.next = node
        
        # Connect the tail sentinel to our new node
        next_pos.prev = node
        
        # Connect our new node to both neighbors
        node.next = next_pos     # Node points forward to tail
        node.prev = prev_mru     # Node points backward to previous MRU item

    def get(self, key: int) -> int:
        """
        Get a value by key. If found, mark it as most recently used.
        Returns -1 if key doesn't exist.
        """
        if key in self.cache:
            node = self.cache[key]
            
            # Move this node to MRU position since we just accessed it
            self.remove_from_list(node)        # Take it out of current position
            self.insert_at_mru_position(node)  # Put it at the MRU end
            
            return node.val
        else:
            return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        """
        Insert or update a key-value pair.
        If at capacity, remove the least recently used item first.
        """
        if key in self.cache:
            # Key already exists - just update the value and mark as MRU
            node = self.cache[key]
            node.val = value  # Update the value
            
            # Move to MRU position since we just accessed it
            self.remove_from_list(node)
            self.insert_at_mru_position(node)
        else:
            # New key - create a new node and add it
            new_node = Node(key, value)
            self.cache[key] = new_node          # Add to hash map
            self.insert_at_mru_position(new_node)  # Add to MRU position in list
        
        # Check if we've exceeded capacity
        if len(self.cache) > self.capacity:
            # Remove the least recently used item (right after head sentinel)
            lru_node = self.head.next
            
            # Remove from both the linked list and hash map
            self.remove_from_list(lru_node)
            del self.cache[lru_node.key]