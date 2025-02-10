class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, num):
        self.heap.append(num)
        self.heapify_up(len(self.heap) - 1)
    
    def heapify_up(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapify_up(parent)
    
    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return max_val
    
    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.heapify_down(largest)
    
    def is_empty(self):
        return len(self.heap) == 0


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        max_heap = MaxHeap()  # Using our custom Max Heap
        stations.append([target, 0])  # Add target as a "dummy station"
        fuel = startFuel
        refuels = 0
        i = 0

        while fuel < target:
            # Add all reachable stations to max heap
            while i < len(stations) and stations[i][0] <= fuel:
                max_heap.insert(stations[i][1])
                i += 1
            
            # If no fuel available, return -1
            if max_heap.is_empty():
                return -1
            
            # Refuel with the largest available fuel
            fuel += max_heap.extract_max()
            refuels += 1

        return refuels
