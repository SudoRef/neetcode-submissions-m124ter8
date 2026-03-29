class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        adj = defaultdict(list)

        for crs,pre in prerequisites:
            adj[pre].append(crs)
            in_degree[crs]+=1
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        res = []

        while q:
            crs = q.popleft()
            res.append(crs)

            for pre in adj[crs]:
                in_degree[pre]-=1
                if in_degree[pre] == 0:
                    q.append(pre)
        return res if len(res) == numCourses else []