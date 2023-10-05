class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        need = len(nums) / 3
        counts = defaultdict(int)
        ans = set()
        for num in nums:
            counts[num] += 1
            if counts[num] > need:
                ans.add(num)

        return ans