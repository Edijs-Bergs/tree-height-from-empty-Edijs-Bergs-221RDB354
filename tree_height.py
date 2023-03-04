import sys
import threading
import numpy as np

def compute_height(n, parents):
    max_height = 0

    # Mark each node as visited or unvisited
    visited = np.zeros(n)

    for i in range(n):
        if visited[i] == 0:
            height = 1
            node = i
            # Traverse the tree upwards from the current node to the root
            while node != -1:
                if visited[node] == 1:
                    height += visited[node]
                    break
                node = parents[node]
                height += 1
                
            # Update the maximum height
            max_height = max(max_height, height)
            
            # Update the visited array
            node = i
            while node != -1 and visited[node] == 0:
                visited[node] = height
                node = parents[node]
                
    return max_height


def main():
    user_input = input().strip()

    if user_input == 'I':
        n = int(input().strip())
        parents = np.array(list(map(int, input().strip().split())))
        print(compute_height(n, parents))
        
    elif user_input == 'F':
        file_name = input().strip()
        file_path = "test/" + file_name
        
        # Make sure the file name does not contain the letter 'a'
        if 'a' in file_name:
            print("Invalid file name")
            return
        
        try:
            with open(file_path, "r") as f:
                n = int(f.readline().strip())
                parents = np.array(list(map(int, f.readline().strip().split())))
                print(compute_height(n, parents))
                
        except:
            print("Error reading file")
            return
        
    else:
        print("Invalid input")
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
