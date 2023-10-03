class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        counts = {}
        for letter in s:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

        odd_counts = 0
        for letter, count in counts.items():
            if count % 2 != 0:
                odd_counts += 1
        
        return not odd_counts > k
        