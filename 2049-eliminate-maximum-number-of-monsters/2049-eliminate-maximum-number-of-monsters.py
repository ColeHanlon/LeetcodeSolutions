class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        reaches_city = []
        for i in range(n):
            reaches_city.append(dist[i] / speed[i])
        
        reaches_city.sort()
        print(reaches_city)
        eliminated = 1
        minutes = 1
        j = 1
        while minutes < n:
            if reaches_city[j] < minutes:
                return eliminated
            elif reaches_city[j] > minutes:
                eliminated += 1
            elif reaches_city[j] == minutes:
                return eliminated
            minutes += 1
            j += 1

        return eliminated