class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        totalheight = 0
        while l<r:
            minheight = min(height[l], height[r])
            width = r - l
            totalheight = max(totalheight, minheight*width)
            if height[l]==minheight:
                l = l + 1
            else:
                r = r - 1    
        return totalheight