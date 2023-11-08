class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x_gap = abs(sx - fx)
        y_gap = abs(sy - fy)

        dist = min(x_gap, y_gap) + abs(y_gap - x_gap)

        if dist == 0:
            return t != 1
        return t >= dist
            