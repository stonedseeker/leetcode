from collections import deque

class Mystack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        return self.arr.append(data)
    
    #Function to remove an item from top of the stack.
    def pop(self):
        return self.arr.pop()

    def __iter__(self):
        return (self.arr)

    def __str__(self):
        return str(self.arr)


class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        print(self.q)
        

    def pop(self) -> int:
        if self.q:
           self.q.popleft() 
        return 0
        

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        if self.q:
            return True

        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()




myStack = MyStack()
print(myStack.push(1))
print(myStack.push(2))
print(myStack.top())
print(myStack.pop())
print(myStack.empty()) 
print(myStack.q)
