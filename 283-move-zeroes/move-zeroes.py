class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        j=i+1
        while j<len(nums) and i<len(nums)-1:
            if nums[i]==0:
                while nums[j]==0 and j<len(nums)-1:
                    j=j+1
                nums[i], nums[j] = nums[j], nums[i] 
            i=i+1
            j=j+1    