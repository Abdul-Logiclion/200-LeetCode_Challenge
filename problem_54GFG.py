class Solution:
    def cloneLinkedList(self, head):
        if head is None:
            return None

        print(head.next.data)  # Just a debug print, optional

        temp = head
        prev = None

        # Use dictionary to map original nodes to their copies
        random_dict = {}

        while temp is not None:
            # If node not already copied, create and store it
            if temp not in random_dict:
                random_dict[temp] = Node(temp.data)

            current = random_dict[temp]  # Get the cloned node

            # Handle random pointer
            if temp.random is not None:
                if temp.random not in random_dict:
                    random_dict[temp.random] = Node(temp.random.data)
                current.random = random_dict[temp.random]

            # Link the previous node's next to the current cloned node
            if prev is not None:
                prev.next = current

            prev = current
            temp = temp.next

        return random_dict[head]  # Return the head of the cloned list