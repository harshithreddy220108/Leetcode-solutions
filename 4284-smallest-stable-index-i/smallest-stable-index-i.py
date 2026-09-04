class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            m_l = max(nums[:i+1])
            m_r = min(nums[i:])
            if m_l-m_r<=k:
                return i
        return -1
