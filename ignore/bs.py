
def binarySearch(ar, target):
    left = 0
    right = len(ar)-1
    while left<=right:
        mid = (left+right)//2
        if ar[mid]==target:
            return mid;
        elif ar[mid]<target:
            left = mid + 1
        else:
            right = mid - 1        
            
    return -1


print(binarySearch([1,3,4,5,6], 15))



