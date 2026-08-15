class Solution(object):
    def romanToInt(self, s):
        x=0
        r={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        for a,b in zip(s,s[1:]):
            if r[a]<r[b]:
                x-=r[a]
            else:
                x+=r[a]
        x+=r[s[-1]]
        return x
        