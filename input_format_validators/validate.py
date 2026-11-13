#!/usr/bin/env python3

# input has form:
# 3
# 1 2 3
# 1 2 3
# 1 2 3

import sys
import re

# read and validate N
n_line = sys.stdin.readline()
assert re.fullmatch(r'[1-9][0-9]*\n?', n_line) # N needs to be a number 

n = int(n_line)
assert 1 <= n <= 10**5

# validate 
for _ in range(n):
    line = sys.stdin.readline()
    
    # must be three positive integers seperated by spaces
    assert re.fullmatch(r'[1-9][0-9]* [1-9][0-9]* [1-9][0-9]*\n', line)
    
    a, b, c = map(int, line.split())
    
    assert 0 <= a <= 10**5
    assert 1 <= b <= 10**5
    assert 1 <= c <= 10**5

assert sys.stdin.readline() == '' # no extra input

sys.exit(42) # valid input, done