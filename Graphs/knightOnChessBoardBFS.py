class Cell:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):
        from collections import deque
        def isInside(x,y,m,n):
            if x >= 1 and y>=1 and x<=m and y<=n:
                return True
            return False
        def solve(a,b,c,d,e,f):
            q = deque()
            q.append(Cell(c,d,0))
            dx = [2,2,1,1,-1,-1,-2,-2]
            dy = [1,-1,2,-2,2,-2,1,-1]
            
            visited = [[False for j in range(b+1)]for i in range(a+1)]
            visited[c][d] = True
            while len(q):
                t = q.popleft()
                
                if t.x == e and t.y == f:
                    return t.d
                for i in range(8):
                    x = t.x+dx[i]
                    y = t.y+dy[i]
                    d = t.d+1
                    if isInside(x,y,a,b) and not visited[x][y]:
                        visited[x][y] = True
                        q.append(Cell(x,y,d))
            return -1
        return solve(A,B,C,D,E,F)
            
