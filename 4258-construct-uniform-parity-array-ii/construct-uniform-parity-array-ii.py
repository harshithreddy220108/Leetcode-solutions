class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        s = min(nums1)
        odd = any(x%2!=0 for x in nums1)
        return s%2!=0 or not odd