class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curmin, curmax = 0, 0
        globmin, globmax = nums[0], nums[0]
        totalsum = 0
        for i in range(0, len(nums)):
            curmin = curmin + nums[i]
            curmax = curmax + nums[i]
            globmin = min(curmin, globmin)
            globmax = max(curmax, globmax)
            if curmax < 0:
                curmax = 0
            if curmin > 0:
                curmin = 0
            totalsum = totalsum + nums[i]
        if globmax<0:
            return globmax
        return max(globmax, totalsum - globmin) 