class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(abs(x))
        r=int(s[::-1])
        if x==r:
            return True
        else:
            return False