class Solution:
    def maxIceCream(self, c: list[int], m: int) -> int:
        c.sort()
        t=0
        for x in c:
            if x<=m:
                m-=x
                t+=1
            else:
                break
        return t