from typing import List


class Solution:
    def __init__(self):
        self.heap = []

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap = []  # Reset heap
        self.insert(nums, k)
        return self.heap[0]  # Root of the heap is the Kth largest element

    def insert(self, array, k):
        for num in array:
            if len(self.heap) < k:
                self.heap.append(num)
                self.heapify_Up(len(self.heap) - 1)
            elif num > self.heap[0]:  # Replace root if num is larger
                self.heap[0] = num
                self.heapify_Down(0, k)

    def heapify_Up(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_Up(parent)

    def heapify_Down(self, index, size):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < size and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_Down(smallest, size)
