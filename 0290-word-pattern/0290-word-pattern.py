class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split(" ")
        a={}
        if len(set(s))!=len(set(pattern)):
            return False
        if len(s)!=len(pattern):
            return False    
        for i in range(0,len(s)):
            if pattern[i] in a:
                if a[pattern[i]]!=s[i]:
                    return False
            else:
                a[pattern[i]]=s[i]
        return True                  
        