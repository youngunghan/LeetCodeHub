class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to track characters in current window
        char_map = {}
        
        # Left pointer of sliding window and result
        left = 0
        max_length = 0
        
        # Right pointer moves through the string
        for right, char in enumerate(s):
            # If character already exists in current window
            if char in char_map and char_map[char] >= left:
                # Move left pointer to skip the duplicate
                left = char_map[char] + 1
            
            # Update character's latest position
            char_map[char] = right
            
            # Update maximum length found so far
            max_length = max(max_length, right - left + 1)
        
        return max_length