class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_vals = {}
        t_vals = {}
        for i in range(0, len(s)):
            if s_vals.get(s[i], None) is not None:
                s_vals[s[i]] = s_vals[s[i]] + 1
            else:
                s_vals[s[i]] = 1

            if t_vals.get(t[i], None) is not None:
                t_vals[t[i]] = t_vals[t[i]] + 1
            else:
                t_vals[t[i]] = 1

        return s_vals == t_vals
