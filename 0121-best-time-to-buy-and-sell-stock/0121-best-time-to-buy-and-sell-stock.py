class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        low_buy = prices[0]
        for price in prices[1:]:
            if price > low_buy:
                max_p = max(max_p, price - low_buy)
            elif price <= low_buy:
                low_buy = price
        return max_p