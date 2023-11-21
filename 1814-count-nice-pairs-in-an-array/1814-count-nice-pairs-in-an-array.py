class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        reverses = [i - int(str(i)[::-1]) for i in nums]
        ans = 0
        for count in Counter(reverses).values():
            ans += count * (count - 1) // 2
        return ans % (10**9 + 7)
