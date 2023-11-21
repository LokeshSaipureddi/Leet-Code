class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=0
        r=len(letters)-1
        a=letters[0]  
        while l<=r:
            m=int((l+r)/2)
            if letters[m]>target and letters[m-1]<=target:
                return letters[m]
            elif letters[m]<=target:
                l=m+1
            else:
                r=m-1       
        return a                 