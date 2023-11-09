class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        left = 0

        for i in range(len(s)):
            if s[i] != s[left]:
                substrings = i - left
                while substrings > 0:
                    ans += substrings
                    substrings -= 1
                left = i
        
        substrings = len(s) - left
        while substrings > 0:
            ans += substrings
            substrings -= 1

        return ans % (10**9 + 7)
