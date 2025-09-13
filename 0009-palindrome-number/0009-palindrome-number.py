class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_ = str(x)
        for i in range(len(str_)):
            if str_[i] != str_[-1 - i]:
                return False
        return True