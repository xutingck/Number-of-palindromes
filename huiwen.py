#coding:utf-8

from numba import jit
import datetime

H1 = 1

@jit
def count(H1, H2):
    z = H1
    n = 0
    
    while z < H2:
        p = str(z)[::-1]
        if z == int(p):
            n += 1
        z += 1

    print "\nBetween {0} and {1} , huiwen numbers is {2}".format(H1, H2, n)

while True:
    H2 = 10 * H1
    startTime = datetime.datetime.now()
    count(H1, H2)
    endTime = datetime.datetime.now()
    print "Start time is {t1}, Cost time is {t2}".format(t1 = startTime, t2 = endTime - startTime)
    H1 *= 10
