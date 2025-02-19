from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Helper function to determine if it's possible to ship all packages
        # within the given number of days with a specified ship capacity.
        def can_ship_with_capacity(max_capacity):
            current_weight = 0  # Tracks the current total weight on the ship for the day.
            day_count = 1       # Starts with the first day.
            
            for weight in weights:
                # Check if adding the current package exceeds the ship's capacity.
                if current_weight + weight > max_capacity:
                    day_count += 1      # Increment the day count since we need an additional day.
                    current_weight = 0  # Reset the current weight for the new day.
                
                current_weight += weight  # Add the current package's weight to the ship's load.
            
            # Return True if the total days required is within the allowed days.
            return day_count <= days

        # Initialize the binary search bounds.
        left = max(weights)  # Minimum possible capacity is the weight of the heaviest package.
        right = sum(weights) # Maximum possible capacity is the sum of all package weights.
        
        # Perform binary search to find the minimum capacity that works.
        while left < right:
            mid = (left + right) // 2  # Calculate the midpoint capacity.
            
            if can_ship_with_capacity(mid):
                right = mid  # If it's possible to ship with this capacity, try a smaller capacity.
            else:
                left = mid + 1  # If not, increase the capacity.
        
        # After the loop, left == right and represents the minimum capacity needed.
        return left
