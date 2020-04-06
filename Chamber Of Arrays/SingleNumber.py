"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""

from collections import defaultdict
def singleNumber_1(nums):
    """
    Time complexity : O(n⋅1)=O(n).
                        Time complexity of for loop is O(n).
                        Time complexity of hash table(dictionary in python) operation pop is O(1.
    Space complexity : O(n)
    """
    hash_table = defaultdict(int)
    for i in nums:
        hash_table[i] += 1    
    for i in hash_table:
        if hash_table[i] == 1:
            return i

def singleNumber_2(nums):
        """
        Time complexity : O(n + n) = O(n). 
                            sum will call next to iterate through nums.
                            We can see it as sum(list(i, for i in nums)) 
                            which means the time complexity is O(n)
                            because of the number of elements(n) in nums.
        Space complexity : O(n + n) = O(n). set needs space for the elements in nums
        """
        return 2 * sum(set(nums)) - sum(nums)

def singleNumber_3(nums):
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        a = 0
        for i in nums:
            a ^= i
        return a 

if __name__ == '__main__':
    input = [[2,2,1],[4,1,2,1,2],[7, 3, 5, 4, 5, 3, 4]]
    for elem in input:
        print("INPUT:",elem)    
        res = singleNumber_3(elem)
        print("OUTPUT:",res)
        print()