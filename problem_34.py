import random

class RandomizedSet:
    def __init__(self):
        # Initialize hashmap and a list to store values for random access
        self.hashmap = {}  # Key: value, Value: index in the list
        self.values = []   # List to store values

    def insert(self, val: int) -> bool:
        # Check if the value already exists in the hashmap
        if val in self.hashmap:
            return False  # Value already exists, return False
        # Add the value to the list and store its index in the hashmap
        self.values.append(val)
        self.hashmap[val] = len(self.values) - 1
        return True  # Value inserted successfully, return True

    def remove(self, val: int) -> bool:
        # Check if the value exists in the hashmap
        if val not in self.hashmap:
            return False  # Value doesn't exist, return False
        # Get the index of the value to be removed
        index = self.hashmap[val]
        # Swap the value with the last element in the list for O(1) removal
        last_value = self.values[-1]
        self.values[index] = last_value
        self.hashmap[last_value] = index
        # Remove the last element from the list and the value from the hashmap
        self.values.pop()
        del self.hashmap[val]
        return True  # Value removed successfully, return True

    def getRandom(self) -> int:
        # Return a random element from the list
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()