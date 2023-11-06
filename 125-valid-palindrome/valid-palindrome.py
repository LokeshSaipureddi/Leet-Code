class Solution:
    def isPalindrome(self, s: str) -> bool:
       string = ("".join(i for i in s if i.isalnum())) 
       string = string.lower()
       return string==string[::-1]