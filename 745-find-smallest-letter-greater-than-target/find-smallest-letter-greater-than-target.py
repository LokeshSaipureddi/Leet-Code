class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=0
        r=len(letters)
        if target<letters[0] or target>=letters[r-1]:
            return letters[0]   
        while l<=r:
            m=int((l+r)/2)
            if letters[m]>target:
                if m!=0 and letters[m-1]<target:
                    return letters[m]        
                r=m-1
            elif letters[m]<target:
                if m!=len(letters)-1 and letters[m+1]>target:
                    return letters[m+1]
                l=m+1
            elif m!=len(letters)-1 and letters[m]==target:
                if letters[m+1]!=target:
                    return letters[m+1]
                l=m+1          