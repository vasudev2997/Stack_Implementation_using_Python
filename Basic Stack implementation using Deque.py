from collections import deque
def stack(l):
    n=input("1. Push  2. Pop  3. Peek\n")
    if(n=='1'):
        for i in range(int(input("Enter the number of terms - "))):
            l.insert(0,input())
    elif(n=='2'):
        if(len(l)>=1):
            l.popleft()
        else:
            print("Stack is Empty")
    elif(n=='3'):
        if(len(l)>=1):
            print(l[0])
        else:
            print("Stack is Empty")
    else:
        print("Invalid Entry")

print("Stack using Deque.")
l=deque()
stack(l)
while(1):
    n=input("Continue Y/N - ")
    if(n=='Y' or n=='y'):
        stack(l)
    elif(n=='N' or  n=='n'):
        break
    else:
        print("Invalid Entry")
print(l)
