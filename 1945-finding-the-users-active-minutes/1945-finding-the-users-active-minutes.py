class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_minutes = defaultdict(set)
        num_users = [0] * k

        for i in range(len(logs)):
            existing = len(user_minutes[logs[i][0]])
            user_minutes[logs[i][0]].add(logs[i][1])

            if existing > 0:
                num_users[existing - 1] -= 1
            
            num_users[len(user_minutes[logs[i][0]]) - 1] += 1

        return num_users