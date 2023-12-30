class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       a=sum(nums)
       n=len(nums)
       b=(n*(n+1))/2
       return int(b-a)