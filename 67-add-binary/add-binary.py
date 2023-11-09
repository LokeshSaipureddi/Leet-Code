class Solution:
    def addBinary(self, a: str, b: str) -> str:
        while len(a)>len(b):
            b="0"+b
        while len(b)>len(a):
            a="0"+a
        k=len(a)-1
        s=""
        p=0
        while k>=0:
            if (a[k]=='0' and b[k]=='1') or (a[k]=='1' and b[k]=='0'):
                if p==1:
                    s='0'+s
                    p=1
                else:    
                    s='1'+s
            elif a[k]=='0' and b[k]=='0':
                if p==1:
                    s='1'+s
                else:
                    s='0'+s
                p=0    
            elif a[k]=='1' and b[k]=='1':
                if p==1:
                    s='1'+s             
                else:
                    s='0'+s
                p=1
            k=k-1 
        if p!=0:
            s="1"+s     
        return s                 