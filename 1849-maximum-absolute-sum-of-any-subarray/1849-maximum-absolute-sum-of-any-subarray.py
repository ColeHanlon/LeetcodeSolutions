class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = max_sum = min_sum = 0
        for x in nums: 
            max_sum = max(max_sum + x, 0)
            min_sum = min(min_sum + x, 0)
            ans = max(ans, max_sum, -min_sum)
        return ans 