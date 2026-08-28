class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        u_c=len(set(candyType))
        m_c=len(candyType)//2
        return min(u_c,m_c)