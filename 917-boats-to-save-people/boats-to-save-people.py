class Solution:
    def numRescueBoats(self, p: list[int], limit: int) -> int:
        p.sort()
        l=0
        r=len(p)-1
        b=0
        while l<=r:
            if p[l]+p[r]<=limit:
                l+=1
            r-=1
            b+=1
        return b
        