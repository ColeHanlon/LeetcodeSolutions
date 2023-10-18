class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        pre_reqs = [0] * (n + 1)
        for parent, child in relations:
            graph[parent].append(child)
            pre_reqs[child] += 1

        course_time = [0] + time
        queue = deque([i for i in range(1, n+1) if pre_reqs[i] == 0])
        
        while queue:
            course = queue.popleft()
            for next_course in graph[course]:
                course_time[next_course] = max(course_time[next_course], course_time[course] + time[next_course-1])
                pre_reqs[next_course] -= 1
                if pre_reqs[next_course] == 0:
                    queue.append(next_course)
        
        return max(course_time)
