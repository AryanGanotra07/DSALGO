class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        import heapq
        c = []
        A.sort(reverse = True)
        B.sort(reverse = True)
        c.append([-1*(A[0] + B[0]),( 0, 0)])
        heapq.heapify(c)
        s =set()
        s.add((0, 0))
        res = []
        for i in range(C):
            tmp = heapq.heappop(c)
            res.append(abs(tmp[0]))
            i = tmp[1][0]
            j = tmp[1][1]
            if i+1 >= len(A) or j+1 >= len(B):
                return res
            sm = A[i+1] + B[j]
            if (i+1, j) not in s:
                s.add((i+1, j))
                heapq.heappush(c, [-1*sm, (i+1, j)])
            sm = A[i] + B[j+1]
            if (i, j+1) not in s:
                s.add((i, j+1))
                heapq.heappush(c, [-1*sm, (i, j+1)])
        return res