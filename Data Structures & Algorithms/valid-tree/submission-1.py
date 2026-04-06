class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        rank = [1] * n
        par = [i for i in range(n)]
        def find(i):
            res = i
            while res != par[res]:
                res = par[res]
            return res

        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                rank[p1]+=rank[p2]
                par[p2] = p1
            else:
                rank[p2]+=rank[p1]
                par[p1] = p2
            return 1
        res = n
        for n1,n2 in edges:
            r = union(n1,n2)
            if r == 0:
                return False
            res-=r
        return res == 1
