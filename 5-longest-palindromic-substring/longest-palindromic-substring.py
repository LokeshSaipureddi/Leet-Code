class Solution:
    def longestPalindrome(self, s: str) -> str:
        result= ""
        resultLen= 0
        for i in range(0,len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if resultLen<r-l+1:
                    result=s[l:r+1]
                    resultLen=r-l+1
                r=r+1
                l=l-1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if resultLen<r-l+1:
                    result=s[l:r+1]
                    resultLen=r-l+1
                r=r+1
                l=l-1
        return result            