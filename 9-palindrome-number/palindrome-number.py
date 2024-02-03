class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        div = 1
        while x >= 10 * div:
            div = div * 10
        while x:
            a = x % 10
            b = x // div
            if a != b:
                return False
            x = (x % div)//10
            div = div / 100
        return True             