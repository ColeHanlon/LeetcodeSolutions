class Solution:
    def candy(self, ratings: List[int]) -> int:
        memo = [1] * len(ratings) 

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                memo[i] = memo[i-1] + 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                memo[i] = max(memo[i], memo[i+1] + 1)
        
        return sum(memo)