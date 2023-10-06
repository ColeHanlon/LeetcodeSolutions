class Solution:
    def integerBreak(self, n: int) -> int:
        max_prod = -1
        for i in range(2, n + 1):
            buckets = [int(n / i)] * i
            curr_bucket = 0
            while sum(buckets) < n:
                buckets[curr_bucket] += 1
                curr_bucket += 1
            max_prod = prod(buckets) if prod(buckets) > max_prod else max_prod

        return max_prod