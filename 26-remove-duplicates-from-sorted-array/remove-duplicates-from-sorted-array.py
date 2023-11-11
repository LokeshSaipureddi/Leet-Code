class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=0
        for i in range(0,len(nums)):
            if nums[i]!=nums[a]:
                a=a+1          
                nums[a]=nums[i]
        return a+1        