class Solution:
    # @param A : integer
    # @return a strings
    def multiple(self, A):
        if A == 1:
            return "1"
        from collections import deque
        visited = set()
        q = deque()
        q.append("1")
        while len(q):
            t = q.popleft()
            if int(t)%A==0:
                return t
            rem = int(t)%A
            q.append(t+"1")
            q.append(t+"0")
        return 0
