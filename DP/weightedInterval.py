# Data structure to store a Job
class Job:
    def __init__(self, start, finish, profit):
 
        self.start = start
        self.finish = finish
        self.profit = profit
 
 
# Function to perform binary search on the given jobs which are sorted by finish time.
# The function returns index of the last job which doesn't conflict with the given job
# i.e. whose finish time is less than or equal to the start time of the given job.
def findLastNonConflictingJob(jobs, n):
 
    # search space
    (low, high) = (0, n)
 
    # iterate till search space is exhausted
    while low <= high:
        mid = (low + high) // 2
        if jobs[mid].finish <= jobs[n].start:
            if jobs[mid + 1].finish <= jobs[n].start:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
 
    # return negative index if no non-conflicting job is found
    return -1
 
 
# Function to print the non-overlapping jobs involved in maximum profit
# using Dynamic Programming
def findMaxProfitJobs(jobs):
 
    # sort jobs in increasing order of their finish times
    jobs.sort(key=lambda x: x.finish)
 
    # get number of jobs
    n = len(jobs)
 
    # maxProfit[i] stores the maximum profit possible for the first i jobs and
    # tasks[i] stores the index of jobs involved in the maximum profit
    maxProfit = [None] * n
    tasks = [[] for _ in range(n)]
 
    # initialize maxProfit[0] and tasks[0] with the first job
    maxProfit[0] = jobs[0].profit
    tasks[0].append(0)
 
    # fill tasks and maxProfit in bottom-up manner
    for i in range(1, n):
 
        # find the index of last non-conflicting job with current job
        index = findLastNonConflictingJob(jobs, i)
 
        # include the current job with its non-conflicting jobs
        currentProfit = jobs[i].profit
        if index != -1:
            currentProfit += maxProfit[index]
 
        # if including the current job leads to the maximum profit so far
        if maxProfit[i - 1] < currentProfit:
            maxProfit[i] = currentProfit
 
            if index != -1:
                tasks[i] = tasks[index]
            tasks[i].append(i)
 
        # excluding the current job leads to the maximum profit so far
        else:
            tasks[i] = tasks[i - 1]
            maxProfit[i] = maxProfit[i - 1]
 
    # maxProfit[n-1] stores the maximum profit
    print("The maximum profit is", maxProfit[n - 1])
 
    # tasks[n-1] stores the index of jobs involved in the maximum profit
    print("The jobs involved in the maximum profit are:", end=' ')
    for i in tasks[n - 1]:
        print((jobs[i].start, jobs[i].finish, jobs[i].profit), end=' ')
 
 
if __name__ == '__main__':
 
    jobs = [
        Job(0, 6, 60), Job(1, 4, 30), Job(3, 5, 10),
        Job(5, 7, 30), Job(5, 9, 50), Job(7, 8, 10)
    ]
 
    findMaxProfitJobs(jobs)
 