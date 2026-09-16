class Solution:
    def canJump(self, nums: list[int]) -> bool:
        m=0
        l=len(nums)-1
        for i in range(len(nums)):
            if i>m:
                return False
            m=max(m,i+nums[i])
            if m>=l:
                return True
        return True