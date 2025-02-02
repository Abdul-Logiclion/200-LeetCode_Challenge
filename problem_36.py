import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.values = []  # List to store all values
        self.hashmap = defaultdict(set)  # Hashmap to store indices of each value

    def insert(self, val: int) -> bool:
        # Add the value to the list and store its index in the hashmap
        self.values.append(val)
        self.hashmap[val].add(len(self.values) - 1)
        # Return True if the value was not present before, otherwise False
        return len(self.hashmap[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.hashmap[val]:
            return False  # Value doesn't exist, return False

        # Get the index of the value to be removed
        index_to_remove = self.hashmap[val].pop()

        # Get the last element in the list
        last_element = self.values[-1]

        # Swap the value to be removed with the last element
        self.values[index_to_remove] = last_element

        # Update the hashmap for the last element
        self.hashmap[last_element].add(index_to_remove)
        self.hashmap[last_element].discard(len(self.values) - 1)
        # Remove the last element from the list
        self.values.pop()
        return True  # Value removed successfully, return True


    def getRandom(self) -> int:
        return random.choice(self.values)