#User function Template for python3
from heapq import heappop, heappush
from typing import List
class Solution:
    
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr: List[int]) -> int:
    
        # code here
        total_cost = 0

        # We start by creating an empty heap
        heap = []
        
        # Insert all the sticks into the heap (heappush will ensure it's a min-heap)
        for stick in arr:
            heappush(heap, stick)
        
        # Continue combining sticks until only one stick is left
        while len(heap) > 1:
            # Pop the two smallest sticks from the heap
            first_smallest = heappop(heap)
            second_smallest = heappop(heap)
            
            # Calculate the cost to combine the two smallest sticks
            combined_cost = first_smallest + second_smallest
            
            # Add the combined cost to the total cost
            total_cost += combined_cost
            
            # Push the combined stick back into the heap
            heappush(heap, combined_cost)
        
        # Return the total cost incurred to combine all sticks
        return total_cost

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import defaultdict
# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minCost(a))

# } Driver Code Ends