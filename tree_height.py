import sys
import threading
import numpy as np

# 4 -1 4 1 1
# 0 1 2 3 4

def compute_height(n, parents):
    # Write this function
    vertiba=0
    max_height = 0
    
    apskatitie = np.zeros(n)
    for i in range(n):
        
        if(apskatitie[i] ==0):
            vertiba=i
            height = np.zeros(n)
            count =0
            while(vertiba >= 0 and height[vertiba] == 0):
                apskatitie[vertiba] = 1
                height[vertiba] = 1
                count+=1
                vertiba = parents[vertiba]
            # for m in range (n):
            #     if (m != vertiba and height[m] !=0):
            #         height[m] +=count
                
            if (count > max_height):
                max_height = count
        # print(max_height)
        # print(i)
        # apskatitie[vertiba] = 1
        # if height[vertiba] != 0:
        #     return np.count_nonzero(apskatitie)
        # height[vertiba] = 1
        # vertiba = parents[vertiba]
        # if i!=0:
        #     for m in range (n):
        #         if (m != vertiba and height[m] !=0):
        #             height[m] +=1
        

    # Your code here
    # return np.count_nonzero(apskatitie)
    return int(max_height)


def main():
    # implement input form keyboard and from files
    ievade = input()
    if 'F' in ievade:
        path = input()
        path = "test/" + path
        if 'a' not in path:
            with open(path, "r") as f:
                    n = int(f.readline())
                    parents = np.array(list(map(int, f.readline().split())))
                    print(compute_height(n, parents))
    if 'I' in ievade:
        n = int(input())
        parents = np.array(list(map(int, input().split())))
        print(compute_height(n, parents))
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
