# Activity-Selection problem
def selectActivity(activities):
 
    # k keeps track of the index of the last selected activity
    k = 0
 
    # set to store the selected activities index
    out = set()
 
    # select 0 as first activity
    out.add(0)
 
    # start iterating from the second element of
    # vector up to its last element
    for i in range(1, len(activities)):
 
        # if start time of i'th activity is is greater or equal
        # to the finish time of the last selected activity, it
        # can be included in activities list
        if activities[i][0] >= activities[k][1]:
            out.add(i)
            k = i  # update i as last selected activity
 
    return out
 
 
if __name__ == '__main__':
 
    # list of given jobs. Each job has an identifier, a deadline and
    # profit associated with it
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9),
                  (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
 
    # Sort the activities according to their finishing time
    activities.sort(key=lambda x: x[1])
 
    result = selectActivity(activities)
    print([activities[i] for i in result])