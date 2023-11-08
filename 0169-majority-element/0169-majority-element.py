class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        possible = -1
        votes = 0
        for num in nums:
            if votes <= 0:
                possible = num
                votes = 1
            else:
                if num == possible:
                    votes += 1
                else:
                    votes -= 1
        
        frequency = 0
        for num in nums:
            if num == possible:
                frequency += 1
        
        return possible if frequency > len(nums) // 2 else -1
