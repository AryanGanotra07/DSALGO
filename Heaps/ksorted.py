class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def mergeKLists(self, A):

        import heapq
        l = []
        for i in range(len(A)):
            l.append([A[i].val,A[i]])
        heapq.heapify(l)
        int_max = float('inf')
        head = ListNode(0)
        curr = head
        while l[0][0] != int_max:
            top = heapq.heappop(l)
            temp = top[1]
            if temp.next is not None:
                heapq.heappush(l,[temp.next.val, temp.next])
            else:
                heapq.heappush(l, [int_max, None])
            curr.next = temp
            curr = temp
        return head.next