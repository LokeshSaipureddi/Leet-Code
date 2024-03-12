class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums= sorted(nums)
        lis=[]
        for i in range(0,len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            a=nums[i]
            l=i+1
            r=len(nums)-1
            while l<r:
                if -a==nums[l]+nums[r]:
                    lis.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif -a<nums[l]+nums[r]:
                    r=r-1
                else:
                    l=l+1
        return lis              