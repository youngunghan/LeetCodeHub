class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome_range(left, right):
            """Helper function to check if substring is palindrome"""
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        # Use two pointers from both ends
        left, right = 0, len(s) - 1
        
        while left < right:
            # If characters match, continue inward
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # First mismatch found - try deleting either character
                # Option 1: Delete left character (skip left pointer)
                # Option 2: Delete right character (skip right pointer)
                return (is_palindrome_range(left + 1, right) or 
                        is_palindrome_range(left, right - 1))
        
        # No mismatch found - already a palindrome
        return True