# minumum waiting time (greedy algorithm)

def minimumWaitingTime(queries):
    queries.sort()
    totalWaitingTime = 0

    for i, v in enumerate(queries):
        print("index", i,"value", v)
        queries_left = len(queries) - (i + 1)
        totalWaitingTime += v * queries_left

    return totalWaitingTime

# ----------------------------------- #

q = [3, 2, 1, 2, 6] # [1,2,2,3,6]=17
print("Result of function call", minimumWaitingTime(q))
