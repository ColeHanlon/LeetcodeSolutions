class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_me = defaultdict(int)
        i_trust = set()

        for relationship in trust:
            i_trust.add(relationship[0])
            trust_me[relationship[1]] += 1

        for person in range(1, n+1):
            if trust_me[person] == n - 1 and person not in i_trust:
                return person
            
        return -1
