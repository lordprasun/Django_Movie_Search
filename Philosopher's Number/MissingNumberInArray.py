"""
Given an array C of size N-1 and given that there are numbers from 1 to N
with one element missing, the missing number is to be found.
Example:
Input:
2
5
1 2 3 5
10
1 2 3 4 5 6 7 8 10

Output:
4
9
"""

def submit_2():
    """
    Possibly your code doesn't work correctly for multiple test-cases (TCs).
    """
    test_cases = int(input())
    for tests in range(test_cases):
        n=int(input())
        xarray = input().split(' ')
        if n-len(xarray) == 1:
            array=[int(float(x)) for x in xarray]
            sumN = (n*(n+1))/2
            print(int(sumN-sum(array)))

def submit_1():
    """
    ValueError: invalid literal for int() with base 10: ''
    """
    test_cases = int(input())
    for tests in range(test_cases):
        n=int(input())
        xarray = input().split(' ')        
        array=[int(x) for x in xarray]
        sumN = (n*(n+1))/2
        print(int(sumN-sum(array)))