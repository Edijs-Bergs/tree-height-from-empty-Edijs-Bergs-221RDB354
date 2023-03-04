import sys
import threading
import numpy as np

def compute_height(n, parents):
    # Write this function
    max_height = 0
    values = 0
    
    
    vievedvalues = np.zeros( n )
    for i in range( n ):
        
        if(vievedvalues[ i ] == 0 ):
            values = i
            height = np.zeros( n )
            count = 0

            while( values >= 0 and height[ values ] == 0 ):
                vievedvalues[ values ] = 1
                height[ values ] = 1
                count = count + 1
                values = parents[ values ]
                
            if ( count > max_height ):
                max_height = count
        
    return int( max_height )


def main():
    # implement input form keyboard and from files
    userinput = input()

    if 'I' in userinput:
        n = int( input() )
        parents = np.array( list(map(int, input().split())) )
        print( compute_height(n, parents) )

    elif 'F' in userinput:
        path = input()
        path = "test/" + path

        if 'a' not in path:
            
            with open( path, "r" ) as f:
                n = int( f.readline() )
                parents = np.array( list(map(int, f.readline().split())) )
                print( compute_height(n, parents) )

        
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
