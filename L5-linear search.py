#Program to implement linear search
flag=0
#to input array
arr=[]
n=int(input("Enter range: "))
for i in range(n):
    ele=int(input())
    arr.append(ele)
#logic begins here
x=int(input("Enter an element to search: "))
for i in range(len(arr)):
    if arr[i] == x:
        print("element is found at index:",i)

