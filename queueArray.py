x = []
class MyQueue:
    #Function to push an element x in a queue.
    def push(self, val):
        return x.append(val)

     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        
        print(x.pop())
         
         # add code here
    def isEmpty(self):
        if len(x) <= 0:
            return True

    

q = MyQueue()

q.push(1)
while True:
    if q.isEmpty():
        break

    inp = input()

    if inp == 1:
        print(q.push(input()))

    if inp == 2:
        q.pop()

