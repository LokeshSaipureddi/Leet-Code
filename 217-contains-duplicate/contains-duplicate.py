class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        i=0
        while(i<len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
            i=i+1    
        return False 