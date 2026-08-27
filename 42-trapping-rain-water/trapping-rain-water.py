class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        m_left=height[left]
        m_right=height[right]
        total=0
        while left<right:
            if m_left<m_right:
                left+=1
                m_left=max(m_left,height[left])
                total+=m_left-height[left]
            else:
                right-=1
                m_right=max(m_right, height[right])
                total+=m_right-height[right]
        return total