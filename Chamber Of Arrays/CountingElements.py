"""
Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.
"""

def countElements(arr):
        prev=-2
        total_count = 0
        curr_count = 0
        for elem in sorted(arr):
            if (elem==prev):
                curr_count += 1
            elif (elem-prev == 1):
                total_count +=curr_count
                total_count +=1
                curr_count = 0
            else:
                curr_count = 0
            prev = elem
        return total_count

if __name__ == '__main__':
    input = [[1,2,3],[1,1,3,3,5,5,7,7],[1,3,2,3,5,0],[1,1,2,2]]
    for elem in input:
        print("INPUT:",elem)    
        res = countElements(elem)
        print("OUTPUT:",res)
        print()