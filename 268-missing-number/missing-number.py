class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       n=len(nums)
       n=(n*(n+1))/2
       s=sum(nums)
       return int(n-s) 