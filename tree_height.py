import sys
import threading
import numpy


def compute_height(n, parents):
    # Initialize an array to keep track of the heights of each node
    heights = [0] * n
    max_height = 0

    # Traverse the tree from each leaf to the root and update the heights array
    for i in range(n):
        node = i
        height = 0
        while node != -1:
            # If we've already computed the height of this node, use that value
            if heights[node] != 0:
                height += heights[node]
                break
            height += 1
            node = parents[node]
        heights[i] = height
        max_height = max(max_height, height)

    return max_height


def main():
    # Read input from file in the "tests" folder
    file_name = input()
    while 'a' in file_name:
        print("File name cannot contain letter 'a'.")
        file_name = input()

    try:
        with open(f"test/{file_name}", "r") as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().strip().split()))
    except:
        print("Error reading file.")
        return

    # Call the compute_height function and print the result
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
