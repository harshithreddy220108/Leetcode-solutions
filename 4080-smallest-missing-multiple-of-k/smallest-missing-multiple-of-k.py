class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiplier = 1
        while True:
            target = k * multiplier
            found = False
            for num in nums:
                if num == target:
                    found = True
                    break
            if not found:
                return target
            multiplier+=1
        