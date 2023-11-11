class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s=int((n*(n+1))/2)
        return s-sum(nums)