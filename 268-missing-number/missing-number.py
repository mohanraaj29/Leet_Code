class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorValue = len(nums)

        for i in range(len(nums)):

            # XOR with expected number
            xorValue ^= i

            # XOR with actual number
            xorValue ^= nums[i]

        return xorValue