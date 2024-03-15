class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        k = -pow(10,6)
        sum = 0
        for i in range(0,len(nums)):
            sum = sum + nums[i]
            k = max(k, sum)
            if sum < 0:
                sum = 0
        return k    


        