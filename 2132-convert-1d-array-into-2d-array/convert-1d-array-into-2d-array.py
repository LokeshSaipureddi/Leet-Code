class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        mn=len(original)
        ll=[]
        k,b=0,n
        if m*n!=mn:
            return []
        for i in range(0,m):
            l=[]
            for j in range(k,b):
                l.append(original[j])    
            ll.append(l)    
            k=b
            b=b+n
        return ll       