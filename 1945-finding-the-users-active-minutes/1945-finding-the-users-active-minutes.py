class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_minutes = defaultdict(set)

        for i in range(len(logs)):
            user_minutes[logs[i][0]].add(logs[i][1])

        num_users = [0] * k

        for key, item in user_minutes.items():
            num_users[len(item) - 1] += 1

        return num_users