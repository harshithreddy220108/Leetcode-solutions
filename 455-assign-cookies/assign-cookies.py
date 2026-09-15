class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        c_i=0
        s_j=0
        while c_i<len(g) and s_j<len(s):
            if s[s_j]>=g[c_i]:
                c_i+=1
                s_j+=1
            else:
                s_j+=1
        return c_i