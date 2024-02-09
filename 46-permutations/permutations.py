class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums.copy()]
        for _ in range(0,len(nums)):
            n = nums.pop(0)
            params = self.permute(nums)
            for p in params:
                p.append(n)
            result.extend(params)
            nums.append(n)
        return result      
        