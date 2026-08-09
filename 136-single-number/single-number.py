class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for i in range(len(nums)):
            a = a ^ nums [i]
        return a
        