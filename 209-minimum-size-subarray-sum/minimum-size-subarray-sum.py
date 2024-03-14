class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0,0
        sum = 0
        length = pow(10,6)
        while l<len(nums) and r<len(nums) and l<=r:
            if sum + nums[r] < target:
                sum = sum + nums[r]
                r = r + 1
            elif sum + nums[r] >= target:
                print(l,r,r-l+1)
                length = min(r-l+1,length)
                sum = sum - nums[l]
                l = l + 1  
        if length == pow(10,6):
            length = 0           
        return length               