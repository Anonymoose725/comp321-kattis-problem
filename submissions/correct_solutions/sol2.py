"""

Idea: Always choose the job with shortest remaining CPU time
      Everytime a new job "arrives", the scheduler takes decides again what job to run

      Jobs are first stored from the input into a list
      Then as the clock moves, they get pushed into a minheap with ready to execute jobs (ready)
      The job is then run until completition or until another job becomes ready to execute
      Time spent waiting by other processes is added to the answer


"""

import sys
import heapq

def solve():
    input_line = sys.stdin.buffer.readline
    n = int(input_line()) #n being the number of jobs

    jobs = [] #store jobs as tuples job_n = (arrival, burst)
    answer = 0

    #Reading input line by line
    for _ in range(n):
        arrival, burst, memory = map(int, input_line().split())
        jobs.append((arrival, burst))
        answer = (answer + memory)
    
    jobs.sort()

    ready = [] #our scheduler minheap queue
    time = 0
    i = 0 #nb of jobs scheduled

    while i < n or ready:
        #no job at the current moment, advance the clock
        if not ready:
            time = max(time, jobs[i][0])

        #query every new job available into the minheap
        while i < n and jobs[i][0] <= time:
            heapq.heappush(ready, jobs[i][1])
            i += 1

        remaining = heapq.heappop(ready)

        #run the job until its done executing or another one arrives
        # remaining: fully executing the curr job ; jobs[i][0] - time: arrival time of next job
        if i < n:
            duration = min(remaining, jobs[i][0] - time)
        else:
            duration = remaining

        answer = (answer + len(ready) * duration) #how many jobs are waiting * last execution duration

        time += duration
        remaining -= duration

        #unfinished jobs are put back in the minheap, and get re evealuated
        if remaining > 0:
            heapq.heappush(ready, remaining)

    print(answer)


if __name__ == "__main__":
    solve()