class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # possible solutions
        # 1.
        # some inner function
        # params: set of current substrings, next letter, 
        # call this inner function for each vowel, for each 1 -> n
        # loop through the existing substrings, adding the next letter
        #    empty set is "base" case, add parameter of curr substring length
        #    for O(1) check for this condition
        # add each new substring to set
        # finally return the len of the set
        #
        # 2.
        # dp solution of similar inner function
        # memoize len of the set at each current substring length
        # add on to the length a function of memo[currLength-1] and possibilities of vowel appending
        # 
        # 3.
        # loop through 1 -> n, and use counters to track possible vowel appending combinations
        MOD = 10**9 + 7        
        a = e = i = o = u = 1

        for length in range(2, n + 1):
            new_a = (e + u + i) % MOD
            new_e = (a + i) % MOD
            new_i = (e + o) % MOD
            new_o = i % MOD
            new_u = (o + i) % MOD

            a, e, i, o, u = new_a, new_e, new_i, new_o, new_u

        count = (a + e + i + o + u) % MOD
        return int(count)