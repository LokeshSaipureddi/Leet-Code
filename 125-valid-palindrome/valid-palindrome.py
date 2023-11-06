class Solution:
    def isPalindrome(self, s: str) -> bool:
       string = ("".join(i for i in s if i.isalnum())) 
       string = string.lower()
       l=0
       r=len(string)-1
       while l<r:
           if string[l]!=string[r]:
               return False
           l=l+1
           r=r-1
       return True   