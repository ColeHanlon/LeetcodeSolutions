class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        unique = set(nums)
        for num in nums:
            if num - 1 not in unique:
                curr = 1
                while (num + curr) in unique:
                    curr += 1
                longest = max(longest, curr)

        return longest
