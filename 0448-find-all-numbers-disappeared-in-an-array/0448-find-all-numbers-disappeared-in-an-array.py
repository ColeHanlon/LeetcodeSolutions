class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        nums_quick = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums_quick:
                ans.append(i)
        return ans
