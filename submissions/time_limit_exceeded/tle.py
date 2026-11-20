"""
Idea: Same strategy as the accepted solution, always run the job with the
      shortest remaining CPU time, and reconsider every time a new job arrives

      This version does NOT use a heap. Every time a decision is needed it
      scans the whole list of processes to find the arrived, unfinished job
      with the smallest remaining time, and scans again to find the next arrival
      The chosen job runs until it finishes or until the next job arrives

      Since it rescans all N processes at every decision it is O(N^2), so it
      times out on large inputs even though the answer it produces is correct
"""

import sys
input = sys.stdin.readline

n = int(input())
arrival = [0] * n
burst = [0] * n
remaining = [0] * n
sumMemory = 0

# read all processes
for i in range(n):
    arrival[i], burst[i], mi = map(int, input().split())
    remaining[i] = burst[i]
    sumMemory += mi

time = 0          # current time
waitingTime = 0
done = 0          # number of processes fully completed

# keep running until all processes are finished
while done < n:

    # find available unfinished job with smallest remaining time
    cur = -1
    best = float('inf')
    for j in range(n):
        if arrival[j] <= time and remaining[j] > 0 and remaining[j] < best:
            best = remaining[j]
            cur = j

    # no job available at current time so jump to the next arrival
    if cur == -1:
        nextJobArrival = float('inf')
        for j in range(n):
            if remaining[j] > 0 and arrival[j] > time and arrival[j] < nextJobArrival:
                nextJobArrival = arrival[j]
        time = nextJobArrival
        continue

    # find when the next job arrives, so we know when to preempt
    nextJobArrival = float('inf')
    for j in range(n):
        if remaining[j] > 0 and arrival[j] > time and arrival[j] < nextJobArrival:
            nextJobArrival = arrival[j]

    # run the process for its full remaining time, or until preempted
    run = min(remaining[cur], nextJobArrival - time)
    time += run
    remaining[cur] -= run

    # process finished
    if remaining[cur] == 0:
        waitingTime += time - arrival[cur] - burst[cur]
        done += 1

print(waitingTime + sumMemory)