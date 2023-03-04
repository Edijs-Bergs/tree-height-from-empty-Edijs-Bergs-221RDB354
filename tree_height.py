import sys
import threading
import numpy
import requests

def compute_height(n, parents):
    # Create a list to store the height of each node
    heights = [0] * n

    # Calculate the height of each node by traversing the tree from bottom to top
    for i in range(n):
        if heights[i] == 0:
            height = 1
            j = parents[i]
            while j != -1:
                if heights[j] != 0:
                    height += heights[j]
                    break
                height += 1
                j = parents[j]
            heights[i] = height

    # Return the maximum height of the tree
    return max(heights)


def main():
    # Ask user to input the file name
    file_name = input("Enter the file name: ")

    # Read the input file from the Github repository
    url = "https://raw.githubusercontent.com//DA-testa/tree-height-from-empty-Edijs-Bergs-221RDB354/main/tests/" + file_name
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the input values
        values = response.text.split()
        n = int(values[0])
        parents = [int(x) for x in values[1:]]

        # Call the compute_height function and print the result
        print(compute_height(n, parents))
    else:
        print("Error: Unable to read file from Github.")


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
