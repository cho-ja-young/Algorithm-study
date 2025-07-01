class Solution:
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        a, b = nums[0], max(nums[0], nums[1])
        for n in nums[2:]:
            a, b = b, max(b, a + n)
        return b