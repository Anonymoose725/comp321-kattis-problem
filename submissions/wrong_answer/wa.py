import sys 
import heapq
input = sys.stdin.readline


n = int(input())
arrival = [0] * n
burst = [0] * n
remaining = [0] * n
sumMemory = 0

# read all processes
for i in range(n):
    arrival[i],burst[i],mi = map(int, input().split())
    remaining[i] = burst[i]
    sumMemory += mi


# build list of process indices, then sort them by arrival time
order = []
for i in range(n):
    order.append(i)

order.sort(key=lambda i: arrival[i])

heap = []
time = 0          # current time
waitingTime = 0
p = 0             # pointer into order

# keep running until all processes are finished
while p < n or heap:

    # no job available, jump time to the next arrival
    if not heap:
        time = max(time, arrival[order[p]])

    # add every job that has arrived by now into the heap
    while p < n and arrival[order[p]] <= time:
        i = order[p]
        heapq.heappush(heap, (remaining[i], i))
        p += 1

    # take the job with the smallest remaining time
    r, cur = heapq.heappop(heap)

    # run the job to completion, never preempting
    run = r
    time += run
    remaining[cur] -= run 

    # job finished, record its waiting time
    waitingTime += time - arrival[cur] - burst[cur]

print(waitingTime + sumMemory)