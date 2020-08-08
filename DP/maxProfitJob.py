# Data structure to store a Job
class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit
 
    def __repr__(self):
        return str((self.start, self.finish, self.profit))
 
 
# Function to print the non-overlapping jobs involved in maximum profit
# using LIS algorithm
def findMaxProfitJobs(jobs):
 
    # sort the jobs according to increasing order of their start time
    jobs.sort(key=lambda x: x.start)
 
    # get number of jobs
    n = len(jobs)
 
    # tasks[i] stores the index of non-conflicting jobs involved in the
    # maximum profit which ends with the i'th job
    tasks = [[] for _ in range(n)]
 
    # maxProfit[i] stores the total profit of jobs in tasks[i]
    maxProfit = [0] * n
 
    # consider every job
    for i in range(n):
        # consider each j less than i
        for j in range(i):
            # update i'th job if j'th job is non-conflicting and leading to the
            # maximum profit
            if jobs[j].finish <= jobs[i].start and maxProfit[i] < maxProfit[j]:
                tasks[i] = tasks[j].copy()
                maxProfit[i] = maxProfit[j]
 
        # end current task with i'th job
        tasks[i].append(i)
        maxProfit[i] += jobs[i].profit
 
    # find index with the maximum profit
    index = 0
    for i in range(1, n):
        if maxProfit[i] > maxProfit[index]:
            index = i
 
    print("The jobs involved in the maximum profit are: ", end='')
    for i in tasks[index]:
        print(jobs[i], end=' ')
 
 
if __name__ == '__main__':
 
    jobs = [
        Job(0, 6, 60),
        Job(5, 9, 50),
        Job(1, 4, 30),
        Job(5, 7, 30),
        Job(3, 5, 10),
        Job(7, 8, 10)
    ]
 
    findMaxProfitJobs(jobs)