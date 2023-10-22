class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left_p, right_p = k, k
        min_val = nums[k]
        max_score = min_val
        
        while left_p > 0 or right_p < len(nums) - 1:
            if left_p == 0 or (right_p < len(nums) - 1 and nums[right_p + 1] > nums[left_p - 1]):
                right_p += 1
            else:
                left_p -= 1
            min_val = min(min_val, nums[left_p], nums[right_p])
            max_score = max(max_score, min_val * (right_p - left_p + 1))
        
        return max_score
