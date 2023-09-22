class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_me = defaultdict(int)
        i_trust = defaultdict(int)

        for relationship in trust:
            i_trust[relationship[0]] += 1
            trust_me[relationship[1]] += 1

        for person in range(1, n+1):
            if trust_me[person] == n - 1 and i_trust[person] == 0:
                return person
            
        return -1
