class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappings = defaultdict(list)

        for word in strs:
            sorted_word = str(sorted(word))

            mappings[sorted_word].append(word)

        return list(mappings.values())
        