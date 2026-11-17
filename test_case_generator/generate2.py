import random

Case = tuple[int, list[tuple[int, int, int]]] # type synonym for simplicity
MAX_N = 10**5
MAX_I = 10**5

def _emit(N: int, procs: list[tuple[int, int, int]], verbose: bool) -> Case:
    """Assembles a test case and prints if needed"""
    if verbose:
        print(N)
        for a, b, m in procs:
            print(a, b, m)
    return (N, procs)


def generate_random_case(n=None, verbose=False) -> Case:
    """Returns (N, [(a, b, m)]), number of processes and each a_i, b_i, m_i"""
    N = n if n is not None else random.randint(1, MAX_N)         # N
    procs = [(random.randint(0, MAX_I),  # a_i
              random.randint(1, MAX_I),  # b_i
              random.randint(1, MAX_I))  # m_i
             for _ in range(N)]
    
    return _emit(N, procs, verbose)


# =============================================================
#  EDGE / BOUNDARY CASES
# =============================================================

def generate_no_overlap_case(verbose=False):
    """
    Returns (N, [(a, b, m)])
    N=2 where the second process arrives only after the first has finished,
    so there is no competition and no preemption. A baseline case.
    """
    procs = [(0, 3, 1),
             (10, 2, 1)]
    return _emit(len(procs), procs, verbose)

def generate_idle_gap_case(k=4, gap=100, verbose=False):
    """
    Returns (N, [(a, b, m)])
    k jobs with a large gap between arrivals, so the CPU finishes one job and
    sits idle until the next arrives. Tests the idle-CPU handling.
    """
    procs = [(i * gap, 3, 1) for i in range(k)]
    return _emit(k, procs, verbose)

def generate_same_arrival_case(k=4, max_b=10, verbose=False):
    """
    Returns (N, [(a, b, m)])
    k jobs that all arrive at t=0 with varied burst times. Every process is
    available from the start with no future arrivals, so it tests pure
    shortest-job ordering.
    """
    procs = [(0, random.randint(1, max_b), random.randint(1, max_b))
             for _ in range(k)]
    return _emit(k, procs, verbose)

def generate_max_values_case(n=3, verbose=False):
    """
    Returns (N, [(a, b, m)])
    n processes with all values at the maximum (a, b, m near 10^5). Checks
    large-number handling. Default n=3 is small enough to verify by hand.
    """
    procs = [(min(i, MAX_I), MAX_I, MAX_I) for i in range(n)]
    return _emit(n, procs, verbose)


# =============================================================
#  PREEMPTION CASES  (catch the non-preemptive Wrong Answer solution)
# =============================================================

def generate_preemption_case(verbose=False):
    """
    Returns (N, [(a, b, m)])
    N=2. One long job starts, then a short job arrives while it is running
    and preempts it. A non-preemptive solution makes the short job wait, so
    this catches the Wrong Answer solution.
    """
    procs = [(0, 10, 1),
             (1, 1, 1)]
    return _emit(len(procs), procs, verbose)

def generate_cascade_case(k=5, long_burst=None, verbose=False):
    """
    Returns (N, [(a, b, m)])
    One long job starts at t=0, then (k-1) short jobs arrive one tick apart
    while it runs. Each short job is much shorter, so it preempts the long
    one, and a non-preemptive solution makes them all wait. Catches the Wrong
    Answer solution. Pass a large k for a big WA + TLE stress case.
    """
    if long_burst is None:
        long_burst = max(k * 2, 100)
    procs = [(0, long_burst, 1)] + [(i, 1, 1) for i in range(1, k)]
    return _emit(k, procs, verbose)


# =============================================================
#  SAMPLE CASES  (small, clear, shown to solvers)
# =============================================================

def generate_sample_statement_example(verbose=False):
    """
    Returns (N, [(a, b, m)])
    The exact example from the problem statement, shown to solvers so they
    can check their understanding. Expected output 10.
    """
    procs = [(0, 5, 2), (1, 2, 1), (2, 1, 3)]
    return _emit(len(procs), procs, verbose)

def generate_sample_minimal_preemption(verbose=False):
    """
    Returns (N, [(a, b, m)])
    A small preemption example shown to solvers. A short job arrives while a
    longer one is running and preempts it. Expected output 3.
    """
    procs = [(0, 4, 1),
             (1, 1, 1)]
    return _emit(len(procs), procs, verbose)

def generate_sample_no_overlap_example(verbose=False):
    """
    Returns (N, [(a, b, m)])
    A small no-overlap example shown to solvers. The second job arrives after
    the first finishes, so neither waits. Expected output 2.
    """
    procs = [(0, 2, 1),
             (5, 3, 1)]
    return _emit(len(procs), procs, verbose)