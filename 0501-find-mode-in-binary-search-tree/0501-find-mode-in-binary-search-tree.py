# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = defaultdict(int)

        stack = [root]
        while stack:
            node = stack.pop()
            counts[node.val] += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        max_count = max(counts.values())
        ans = []
        for key, value in counts.items():
            if value == max_count:
                ans.append(key)

        return ans

