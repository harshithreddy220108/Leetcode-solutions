class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def g(a,b):
            while b:
                a,b=b,a%b
            return a
        t=0
        c=[0]*10
        for x in nums:
            l=x%10
            for i in range(1,10):
                if c[i]>0 and g(i,l)==1:
                    t+=c[i]
            d=x
            while d>=10:
                d//=10
            c[d]+=1

        return t