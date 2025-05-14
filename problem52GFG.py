class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # Initialize two pointers, both starting at the head of the list
        slow = head
        fast = head

        # Traverse the list with two pointers:
        # - slow moves one step at a time
        # - fast moves two steps at a time
        while fast and fast.next:
            slow = slow.next          # Move slow pointer by one step
            fast = fast.next.next     # Move fast pointer by two steps

            # If slow and fast meet at the same node, there is a loop
            if slow == fast:
                return True

        # If the loop ends (fast reached the end), there is no cycle
        return False
