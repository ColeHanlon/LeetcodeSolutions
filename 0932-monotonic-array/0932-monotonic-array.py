class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        increasing = False
        first = nums[0]
        for num in nums:
            if num != first:
                increasing = True if num > first else False
                break

        for i in range(len(nums)-1):
            if increasing and nums[i] > nums[i+1]:
                return False
            elif not increasing and nums[i] < nums[i+1]:
                return False

        return True
