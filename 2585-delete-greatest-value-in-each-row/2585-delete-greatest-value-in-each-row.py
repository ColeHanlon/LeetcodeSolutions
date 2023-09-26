class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        max_sum = 0

        for i in range(len(grid)):
            grid[i].sort()
        
        while len(grid[0]):
            iter_max = 0
            for i in range(len(grid)):
                iter_max = max(iter_max, grid[i].pop())
            max_sum += iter_max

        return max_sum