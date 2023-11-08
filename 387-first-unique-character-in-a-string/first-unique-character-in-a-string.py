class Solution:
    def firstUniqChar(self, s: str) -> int:
        a={}
        for char in s:
            a.setdefault(char,0)
            a[char]= a[char]+1
        for i in range(0,len(s)):
            if a[s[i]]==1:
                return i 
        return -1            