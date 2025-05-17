from collections import OrderedDict

class LRUCache:
    """
    This is an alternative implementation of an LRU (Least Recently Used) Cache using Python's built-in OrderedDict.

    LRU cache is used to store a fixed number of key-value pairs such that when the cache is full, 
    the least recently used item is removed to make space for new entries.

    Data Structures Used:
    ---------------------
    - OrderedDict:
        A subclass of dict that remembers the order keys were inserted.
        This is ideal for LRU, because we want to keep track of the usage order.
        - Keys at the beginning are least recently used.
        - Keys at the end are most recently used.

    - No need for a separate doubly linked list and hashmap manually — OrderedDict handles both functionalities.

    Time Complexity:
    ----------------
    - get/put operations: O(1) average-case time
    """

    capacity: int                 # Maximum number of items the cache can hold
    cache_map: OrderedDict        # Stores the cache data in access order

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = OrderedDict()

    def get(self, key: int) -> int:
        """
        Retrieve the value for the given key from the cache.

        If the key exists:
            - Move it to the end (mark as recently used)
            - Return its value
        Else:
            - Return -1 (key not found)
        """
        if key not in self.cache_map:
            return -1

        value = self.cache_map[key]
        self.cache_map.move_to_end(key)  # Mark as most recently used by moving to end

        return value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update the value for the given key in the cache.

        If the key already exists:
            - Update its value
            - Move it to the end (mark as recently used)

        If the key doesn't exist:
            - If the cache is full:
                - Remove the least recently used item (first item in OrderedDict)
            - Insert the new key-value pair at the end
        """

        if key in self.cache_map:
            # Update value and mark as recently used
            self.cache_map[key] = value
            self.cache_map.move_to_end(key)
            return

        if len(self.cache_map) >= self.capacity:
            # Remove the least recently used key (first key in OrderedDict)
            # OrderedDict preserves insertion order, so first = LRU
            lru_key = next(iter(self.cache_map))  # O(1)
            del self.cache_map[lru_key]           # O(1)

        # Add new key-value pair at the end (most recently used)
        self.cache_map[key] = value
