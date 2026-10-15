class Solution:
    def bagOfTokensScore(self, t: list[int], p: int) -> int:
        t.sort()
        l = 0
        r = len(t) - 1
        s = 0
        m = 0
        while l <= r:
            if p >= t[l]:
                p -= t[l]
                s += 1
                l += 1
                m = max(m, s)
            elif s > 0:
                p += t[r]
                s -= 1
                r -= 1
            else:
                break
        return m
