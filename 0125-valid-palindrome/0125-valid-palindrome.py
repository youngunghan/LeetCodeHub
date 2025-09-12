class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers from both ends
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from left
            if not s[left].isalnum():
                left += 1
                continue
                
            # Skip non-alphanumeric characters from right
            if not s[right].isalnum():
                right -= 1
                continue
                
            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
                
            # Move both pointers inward
            left += 1
            right -= 1
        
        return True