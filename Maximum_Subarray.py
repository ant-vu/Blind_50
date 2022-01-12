class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max, max_till_now = 0, -inf
        for i in nums:
            cur_max = max(i, cur_max + i)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now
