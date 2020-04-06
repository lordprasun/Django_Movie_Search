"""
Given an array of integers, find the first repeating element in it
"""

def DoubleNumber(arr):
    n = len(arr)
    Min = -1
    myhash = dict()
    for i in range(n-1,-1,-1):
        if arr[i] in myhash.keys():
            Min = i
        else:
            myhash[arr[i]]=1
    return arr[Min]
    

if __name__ == '__main__':
    input = [[10, 5, 3, 4, 3, 5, 6],[6, 10, 5, 4, 9, 120, 4, 6, 10],[7, 3, 5, 4, 5, 3, 4]]
    for elem in input:
        print("INPUT:",elem)    
        res = DoubleNumber(elem)
        print("OUTPUT:",res) #If res = -1 there is no repeating element
        print()