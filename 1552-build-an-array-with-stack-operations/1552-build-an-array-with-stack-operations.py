class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        built_target = []
        unique_vals = set(target)
        for i in range(1, target[-1] + 1):
            if i in unique_vals:
                built_target.append("Push")
            else:
                built_target.append("Push")
                built_target.append("Pop")
        return built_target