#121910313025
#program to implement linear search by user defined functions
def linearSearch(arr,n,x):

    #logic begins here
    for i in range(0,n):
        if(arr[i] == x):
            return i
    return -1
#input values
arr=[25,4,3,1,8]
x=3
n=len(arr)
#calling function
result=linearSearch(arr,n,x)
if(result == -1):
    print("element is not found")
else:
    print("element is found at index:",result)
