class Solution:
    def isValid(self, s: str) -> bool:
        h={")":"(","}":"{","]":"["}
        l=[]
        i=0
        while i<len(s):
            if s[i] not in h:
                l.append(s[i])
            elif s[i] in h:    
                if len(l)==0 or h[s[i]]!=l.pop(-1):
                    return False  
            i=i+1          
        return len(l)==0