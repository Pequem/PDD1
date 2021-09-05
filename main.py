import math
import time
from concurrent import futures
from multiprocessing import freeze_support
import numpy


topLimit = 5000


def sort(vec):
    vec.sort()
    return vec

# An optimized version of Bubble Sort
def bubbleSort(arr):
    n = len(arr)
   
    # Traverse through all array elements
    for i in range(n):
        swapped = False
  
        # Last i elements are already
        #  in place
        for j in range(0, n-i-1):
   
            # traverse the array from 0 to
            # n-i-1. Swap if the element 
            # found is greater than the
            # next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
  
        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break
    return arr


if __name__ == '__main__':

    ks = [1, 2, 4, 8]

    results = {'1':0, '2': 0, '4': 0, '8': 0}

    referenceVec = numpy.random.randint(1, topLimit, topLimit)
    freeze_support()

    executor = futures.ProcessPoolExecutor(8)

    for _ in range(10):
        for k in ks:
            print('Ordenando com ' + str(k) + ' processos')
            _k = k
            vec = referenceVec[:]

            startTime = time.time()
            while True:
                threads = []
                vecLength = topLimit / k
                
                for i in range(k):
                    tempVec = vec[int(vecLength*i):int(vecLength*(i+1))]
                    t = executor.submit(bubbleSort, tempVec)
                    threads.append(t)
                
                vec = []
                for t in threads:
                    result_vec = t.result()
                    vec = numpy.append(vec, result_vec)

                k = math.floor(k/2)
                if k <= 0:
                    break
            duration = time.time() - startTime
            results[str(_k)] += duration/10
            print('Tempo gasto' + str(duration) + '\n\n')

    for k in ks:
        print('tempo medio k:'+str(k)+':'+str(results[str(k)]))