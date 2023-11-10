class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a,b={},{}
        for c1,c2 in zip(s,t):
            if ((c1 in a) and (a[c1]!=c2)) or ((c2 in b) and (b[c2]!=c1)):
                return False
            a[c1]=c2
            b[c2]=c1       
        return True    