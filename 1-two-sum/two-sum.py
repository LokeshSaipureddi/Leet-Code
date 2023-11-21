class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l={}
        for i in range(0,len(nums)):
            if nums[i] in l:
                return [l[nums[i]],i]
            else:
                l[target-nums[i]]=i