class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstpos, lastpos = -1, -1
        left = 0
        right = len(nums) - 1
        flag = 0
        while right >= left and not flag:
            midvalue = int((left + right)/2)
            if nums[midvalue] < target:
                left = left + 1
            elif nums[midvalue] > target:
                right = right - 1
            elif nums[midvalue] == target:
                firstpos, lastpos = midvalue, midvalue
                while firstpos >= 0 and nums[firstpos] == target:
                    firstpos -=1
                while lastpos <= len(nums)-1 and nums[lastpos] == target:
                    lastpos +=1
                firstpos += 1
                lastpos -= 1
                flag = 1
        return [firstpos, lastpos]