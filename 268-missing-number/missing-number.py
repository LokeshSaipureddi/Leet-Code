class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s=int((n*(n+1))/2)
        new=sum(nums)
        return s-new