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


def generate_random_case(verbose=False) -> Case:
    """Returns (N, [(a, b, m)]), number of processes and each a_i, b_i, m_i"""
    N = random.randint(1, MAX_N)         # N
    procs = [(random.randint(0, MAX_I),  # a_i
              random.randint(1, MAX_I),  # b_i
              random.randint(1, MAX_I))  # m_i
             for _ in range(N)]
    
    return _emit(N, procs, verbose)
    
def generate_realistic_case(max_n=6, max_i=6, verbose=False):
    """
    Returns (N, [(a, b, m)])
    Within custom constraints, with realistic and readable defaults 
    ex. max 6 processes
    """
    N = random.randint(1, max_n)
    procs = [(random.randint(0, max_i), 
              random.randint(1, max_i), 
              random.randint(1, max_i))
             for _ in range(N)]  
    
    return _emit(N, procs, verbose)  

def generate_left_edge_case(eps=3, verbose=False):
    """
    Returns (N, [(a, b, m)])
    Values are close to their minimums: N in [1, 1+eps],
    a in [0, eps], b and m in [1, 1+eps].
    Heavy on ties (same arrival, same burst), which is where schedulers break.
    """
    N = random.randint(1, 1 + eps)
    procs = [(random.randint(0, eps),
              random.randint(1, 1 + eps),
              random.randint(1, 1 + eps))
             for _ in range(N)]
    
    return _emit(N, procs, verbose)

def generate_right_edge_case(eps=3, verbose=False):
    """
    Returns (N, [(a, b, m)])
    Values are close to their maximums: N in [MAX_N - eps, MAX_N],
    a, b, m in [MAX_I - eps, MAX_I].
    Stresses overflow and performance.
    """
    N = random.randint(MAX_N - eps, MAX_N)
    procs = [(random.randint(MAX_I - eps, MAX_I),
              random.randint(MAX_I - eps, MAX_I),
              random.randint(MAX_I - eps, MAX_I))
             for _ in range(N)]
    
    return _emit(N, procs, verbose)