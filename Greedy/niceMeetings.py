
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        import heapq
        meet=sorted(A,key=lambda x:x[0])
        heap=[]
        for i in range(len(meet)):
            if heap and meet[i][0]>=heap[0]:
                heapq.heapreplace(heap,meet[i][1])
            else:
                heapq.heappush(heap,meet[i][1])
        return len(heap)
            
