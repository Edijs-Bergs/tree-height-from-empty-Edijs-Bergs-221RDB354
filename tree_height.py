# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Initialize an array to keep track of the heights of the nodes
    heights = [0] * n

    # Calculate the height of each node in a bottom-up fashion
    for i in range(n):
        if heights[i] == 0:  # Node i hasn't been visited yet
            height = 1  # Height of the current node
            j = i  # Index of the parent of the current node

            while parents[j] != -1:
                if heights[j] != 0:  # Height of parent j has already been calculated
                    height += heights[j]
                    break
                height += 1
                j = parents[j]

            heights[i] = height

    # Return the maximum height
    return max(heights)


def main():
    # Read the input file
    filename = input("Enter the filename: ")
    if 'a' in filename:
        print("Invalid filename")
        return

    try:
        with open(filename) as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    except FileNotFoundError:
        print("File not found")
        return

    # Calculate the height of the tree
    height = compute_height(n, parents)

    # Print the result
    print(height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
