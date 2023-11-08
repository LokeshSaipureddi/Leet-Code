class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=set()
        for i in range(0,len(nums1)):
            if nums1[i] in nums2:
                l.add(nums1[i])
        return list(l)                