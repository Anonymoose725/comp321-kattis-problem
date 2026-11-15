import sys
import heapq

MOD = 1_000_000_007


def solve():
    input_line = sys.stdin.buffer.readline
    n = int(input_line())

    jobs = [] #store jobs as tuples job_n = (arrival, burst)
    answer = 0

    for _ in range(n):
        arrival, burst, memory = map(int, input_line().split())
        jobs.append((arrival, burst))
        answer = (answer + memory) % MOD

    jobs.sort()

    ready = []
    time = 0
    i = 0

    while i < n or ready:
        if not ready:
            time = max(time, jobs[i][0])

        while i < n and jobs[i][0] <= time:
            heapq.heappush(ready, jobs[i][1])
            i += 1

        remaining = heapq.heappop(ready)

        if i < n:
            duration = min(remaining, jobs[i][0] - time)
        else:
            duration = remaining

        answer = (answer + len(ready) * duration) % MOD

        time += duration
        remaining -= duration

        if remaining > 0:
            heapq.heappush(ready, remaining)

    print(answer)


if __name__ == "__main__":
    solve()