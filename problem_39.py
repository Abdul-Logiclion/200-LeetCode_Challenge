from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # HashMap to store the frequency of characters in t
        t_count = Counter(t)
        window_count = {}

        left = 0
        min_length = float("inf")
        min_window = ""
        required_chars = len(t_count)  # Unique characters required
        formed = 0  # Unique characters satisfied in current window

        for right in range(len(s)):
            # Expand window by adding right character
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            # If this character reaches the required frequency in t, update `formed`
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            # Contract window when all required characters are satisfied
            while formed == required_chars:
                # Update the minimum window if it's smaller
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right+1]

                # Remove left character and update counts
                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    formed -= 1
                
                left += 1  # Shrink window

        return min_window
