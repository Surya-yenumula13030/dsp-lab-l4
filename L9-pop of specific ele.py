#121910313025
#To pop a specific element from stack
stack=[]
n=int(input("Enter number of elements:"))
print("Enter elements")
#append function to push
for i in range(0,n):
    ele=int(input())
    stack.append(ele)
print("Initial stack is :")
print(stack)
      
#pop() function to pop

print("enter an index of element to pop:")
p=int(input())
stack.pop(p)
#display
print("stack after elements are poped:")
print(stack)


    
