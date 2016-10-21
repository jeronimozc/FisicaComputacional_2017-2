from multiprocessing import Pool
from contextlib import closing
import time

def f(x, s=2000):
    for j in xrange(10000):
        out = s
        for i in xrange(1,s):
            out *= i
    return x

with closing(Pool(processes=8)) as pool:
    print pool.map(f, [1,2,3])
    pool.terminate()
