class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize previous node as None (new end of the list)
        prev = None
        # Start with the current node as head
        current = head
        
        # Traverse the linked list
        while current:
            # Store the next node before breaking the link
            next_node = current.next
            # Reverse the current node's pointer
            current.next = prev
            # Move prev and current one step forward
            prev = current
            current = next_node
        
        # At the end, prev will be the new head of the reversed list
        return prev
