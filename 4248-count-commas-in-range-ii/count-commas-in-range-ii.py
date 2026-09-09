class Solution:
    def countCommas(self, n: int) -> int:
        c=0
        s=1000
        while s<=n:
            c+=(n-s+1)
            s*=1000
        return c