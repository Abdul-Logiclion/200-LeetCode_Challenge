class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # If the list is empty, return 0
        if not nums:
            return 0
        
        # Step 1: Store all the elements in a set for O(1) lookups
        hashmap = set(nums)
        
        maxStreak = 0
        
        # Step 2: Iterate through the set
        for num in hashmap:
            # Check if 'num' is the start of a sequence
            if num - 1 not in hashmap:
                currentStreak = 1
                currentNum = num
                
                # Step 3: Count consecutive numbers starting from 'num'
                while currentNum + 1 in hashmap:
                    currentNum += 1
                    currentStreak += 1
                
                # Update the max streak length
                maxStreak = max(maxStreak, currentStreak)
        
        return maxStreak
