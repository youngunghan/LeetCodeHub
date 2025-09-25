class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # minimum count of '(' characters
        high = 0  # maximum count of '(' characters
        
        for char in s:
            if char == '(':
                low += 1   # increment both counters for '('
                high += 1
            elif char == ')':
                low -= 1   # decrement both counters for ')'
                high -= 1
            else:  # char == '*'
                low -= 1   # treat '*' as ')' or empty string (minimum case)
                high += 1  # treat '*' as '(' (maximum case)
            
            # if high becomes negative, too many ')' characters
            if high < 0:
                return False
            
            # reset low to 0 if negative (ignore unnecessary ')')
            low = max(low, 0)
        
        # valid if we can balance all parentheses (low == 0)
        return low == 0