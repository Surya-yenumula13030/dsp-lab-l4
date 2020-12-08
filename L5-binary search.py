#121910313025
#Program to implement binary search
def binarySearch(arr,low,high,x):
    #check base case
    if high >= low:
        mid=(high+low) //2
        #if element is present at middle itself
        if arr[mid] == x:
            return mid
        #if element is smaller than mid,then it can only be left in subarray
        elif arr[mid] > x:
            return binarySearch(arr,low,mid-1,x)
        #else it can be present in right subarray
        else:
            return binarySearch(arr,mid+1,high,x)
    else:
        #element is not present in array
        return -1
#test array
arr=[10,15,24,67,98,240]
x=67
#function call
result=binarySearch(arr,0,len(arr)-1,x)

if result != -1:
    print("element is present at index",str(result))
else:
    print("element is not found in array")
