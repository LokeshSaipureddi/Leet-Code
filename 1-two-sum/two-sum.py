class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index={}
        for i in range(0,len(nums)):
            if target-nums[i] not in index.keys():
                index[nums[i]]=i
            else:
                return [index[target-nums[i]],i]    