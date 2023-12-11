class Solution:
    def reverse(self, x: int) -> int:
        k=0
        if x<0:
            k=1
            x=-x
        x = str(x)    
        a = int(x[::-1])
        if a > 2147483647 or a< - 2147483648:
            return 0
        if k==1:
            return -int(x[::-1])
        return int(x[::-1])
        