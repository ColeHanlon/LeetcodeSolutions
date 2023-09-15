class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vals = {}

        for i in range(0, len(nums)):
            if vals.get(nums[i], None):
                return True
            
            vals[nums[i]] = True

        return False