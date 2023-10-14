class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        total_walls = len(cost)
        
        @cache
        def recursive_dp(curr_wall, num_remaining):
            if num_remaining <= 0:
                return 0
            elif curr_wall == total_walls:
                return inf
            
            return min(cost[curr_wall] + recursive_dp(curr_wall + 1, num_remaining - time[curr_wall] - 1),
                       recursive_dp(curr_wall + 1, num_remaining))

        return recursive_dp(0, total_walls)