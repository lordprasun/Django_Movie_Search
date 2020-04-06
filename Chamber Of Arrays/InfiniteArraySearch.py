"""
Find position of an element in a sorted array of infinite numbers
"""

def binarySearch(arr,l,h, key):
    # print(l,h,arr)   
    if h >= l:
        mid = (l+h)//2
        # print(mid)
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            return binarySearch(arr,l,mid-1,key)
        else:
            return binarySearch(arr,mid+1,h,key)
    return -1


def findPos(arr,key):
    l,h,val=0,1,arr[1]
    while val < key: # Array is sorted in ascending order
        l = h
        h = h*2
        val = arr[h] 
    res = binarySearch(arr,l,h,key) 
    return res     
    # res = binarySearch(arr[l:h+1],0,h-l,key)
    # if res != -1:
    #     return res+l
    # else:
    #     return res


if __name__ == '__main__':
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170] 
    ans = findPos(arr,130) 
    if ans == -1: 
        print ("Element not found")
    else: 
        print("Element found at index",ans)