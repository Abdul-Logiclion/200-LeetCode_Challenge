class Solution:
    # Function to find the middle element of the linked list.
    def findMiddle(self, head):
        # Initialize two pointers, both starting at the head of the list
        slow = head
        fast = head

        # Traverse the list with two pointers:
        # - slow moves one step at a time
        # - fast moves two steps at a time
        while fast and fast.next:
            slow = slow.next          # Move slow pointer by one step
            fast = fast.next.next     # Move fast pointer by two steps

        # When fast reaches the end, slow will be at the middle
        return slow
