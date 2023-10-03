class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        pairs = 0
        for num in nums:
            if num in counts:
                pairs += counts[num]
            counts[num] += 1
        
        return pairs