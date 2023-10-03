class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = -1
        sec_max = -1
        for num in nums:
            if num >= maximum:
                sec_max = maximum
                maximum = num
            elif num >= sec_max:
                sec_max = num
        
        return (maximum - 1) * (sec_max - 1)