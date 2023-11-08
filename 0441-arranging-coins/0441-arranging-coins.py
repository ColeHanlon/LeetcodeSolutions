class Solution:
    def arrangeCoins(self, n: int) -> int:
        curr_row = 0
        while n >= curr_row + 1:
            curr_row += 1
            n -= curr_row

        return curr_row