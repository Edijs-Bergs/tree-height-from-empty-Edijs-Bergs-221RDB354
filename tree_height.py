import sys
import threading
import numpy as np

def compute_height(n, parents):
    

    value=0 #vertiba
    max_height = 0 #maksimalais augstums
    

    vieveditems = np.zeros(n) #apskatītās lietas
    for i in range(n):
        
        if(vieveditems[i] ==0):

            value=i
            height = np.zeros(n) #augstums
            counter =0 # skaititajs

            while(value >= 0 and height[value] == 0):

                vieveditems[value] = 1
                height[value] = 1
                counter+=1
                value = parents[value]
                
            if (counter > max_height):

                max_height = counter
        
    return int(max_height)


def main():
    
    userinput = input() # lietotaja ievade

    if 'F' in input:

        filepath = input() #lietotaja ievade
        filepath = "test/" + filepath

        if 'a' not in filepath: # parbaudam vai satur a

            with open(filepath, "r") as f:

                n = int(f.readline())
                parents = np.array(list(map(int, f.readline().split()))) #read split line
                print(compute_height(n, parents))

    if 'I' in userinput: # lietotaja ievads i
        
        n = int(input())
        parents = np.array(list(map(int, input().split())))
        print(compute_height(n, parents))
    
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
