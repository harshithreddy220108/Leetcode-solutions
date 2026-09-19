class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        c_t=0
        s_s=0
        for i in range(len(gas)):
            c_t+=gas[i]-cost[i]
            if c_t<0:
                s_s=i+1
                c_t=0
        return s_s