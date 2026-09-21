class Solution:
    def reverseDegree(self, s: str) -> int:
        total=0
        for i, char in enumerate(s):
            reverse_pos=26-(ord(char)-ord('a'))
            total+=reverse_pos*(i+1)
        return total