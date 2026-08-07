class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        pre=1
        post=1
        r=[0]*n
        for i in range(n):
            r[i]=pre
            pre*=nums[i]
        for i in range(n-1,-1,-1):
            r[i]*=post
            post*=nums[i]
        return r
        