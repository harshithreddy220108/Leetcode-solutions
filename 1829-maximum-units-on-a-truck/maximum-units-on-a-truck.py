class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        t_u=0
        for n_b, upb in boxTypes:
            btk=min(n_b,truckSize)
            t_u+=btk*upb
            truckSize-=btk
            if truckSize==0:
                break
        return t_u