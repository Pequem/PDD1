import random
import math
import time
import threading
import numpy

topLimit = 50000000

def generateVector():
    vec = []
    for i in range(topLimit):
        vec.append(random.uniform(0, topLimit))
    return vec


def sort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        sort(lefthalf)
        sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def sort2(vec):
    vec.sort()

ks = [1, 2, 4, 8]

for k in ks:
    print('Ordenando com ' + str(k) + ' processos')
    vec = numpy.random.randint(1, topLimit, topLimit)
    startTime = time.time()
    while True:
        threads = []
        vecLength = topLimit / k

        for i in range(k):
            t = threading.Thread(target=sort, args=(vec[int(vecLength*i):int(vecLength*(i+1))], ))
            t.start()
            threads.append(t)
        for t in threads:
            result_vec = t.join()

        k = math.floor(k/2)
        if k <= 0:
            break
    duration = time.time() - startTime
    print('Tempo gasto' + str(duration) + '\n\n')