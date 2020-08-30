class stack():      #Main Class for Stack
    def __init__(self, stacklength):     
        self.stack=[]   #Stack Declaration
        self.length=stacklength-1       #Length of Stack
        self.start=-1       #Start Position Initialized to -1
        
    def push(self,value):   
        if(self.start<self.length):
            self.stack.append(value)
            self.start+=1
            print("Item Added to Stack.")
            return True
        else:
            print("Stack is Full.")
            return False
        
    def pop(self):
        if(self.start>-1):
           print("{} Removed From Stack.".format(self.stack.pop()))
           self.start-=1
           return True
        else:
            print("Stack is Empty")
            return False
        
    def peek(self):
        if(self.start>-1):
            print(self.stack[-1])
        else:
            print("Stack is Empty.")
            
def operation(stacklength):   
    print("1. Push  2.Pop   3.Peek")       #List for Implementation Options
    n=int(input("Enter Your Input - "))
    if(n==1):       #Push
        item=int(input("Enter the Number of items To Be Inserted : "))
        if(item<=stacklength):
            for i in range(item):
                Item=input()
                addstack.push(Item)
        else:
            print("Invalid Entry.")
            return False
        
    elif(n==2):       #Pop
        addstack.pop()
        
    elif(n==3):       #Peek
        addstack.peek()
        
    else:
        print("Invalid Entry")

stacklength=int(input("Enter the Length of Stack : "))    #Main Body
addstack=stack(stacklength)     #Specifying Length of Stack
operation(stacklength)
while(1):
    c=input("Continue Y/N : ")
    if(c=="Y" or c=="y"):
        operation(stacklength)
    elif(c=="N"  or c=="n"):
        break
    else:
        print("Invalid Entry.")
