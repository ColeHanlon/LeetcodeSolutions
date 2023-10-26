class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        tree_counts = defaultdict(int)

        for a in arr:
            curr_count = 1
            for b in arr:
                if b > a:
                    break
                
                curr_count += (tree_counts[b] * tree_counts[a/b])

            tree_counts[a] = curr_count

        return sum(tree_counts.values())%(10**9+7)