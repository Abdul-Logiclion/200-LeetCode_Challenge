class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        maxAnagram = 0
        currentAnagram = 0
        index = 0
        array = []
        p_sorted = sorted(p)  # Sort `p` once for comparison

        for i in range(len(s)):
            if i >= len(p) - 1:  # Check only when we have at least `len(p)` characters
                window = s[i - len(p) + 1: i + 1]  # Extract the current window
                if sorted(window) == p_sorted:  # Compare sorted versions
                    maxAnagram += 1
                    array.append(i - len(p) + 1)  # Corrected index tracking
                
            index += 1  # Continue moving index forward

        print(maxAnagram, array)
        return array