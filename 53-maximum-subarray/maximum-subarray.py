class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        k=float(-inf)
        sum=0
        for i in range(0,len(nums)):
            sum=sum+nums[i]
            k=max(k,sum)
            if sum<0:
                sum=0
        return k