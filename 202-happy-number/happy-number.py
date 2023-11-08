class Solution:
    def isHappy(self, n: int) -> bool:
        v=set()
        while n not in v:
            v.add(n)
            n=self.squares(n)
            if n==1:
                return True
        return False 

    def squares(self,n: int)->int:
        sum=0
        while n!=0:
            b=n%10
            b=b**2
            sum=sum+b
            n=n//10 
        return sum          