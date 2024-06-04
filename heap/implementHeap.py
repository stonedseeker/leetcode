class Heap:
    def __init__(self):
        self.children = []

    def insert(self, value):
        self.children.append(value)
        if len(self.children) > 1:
            for i in range(len(self.children) - 1, -1, -1):
               if self.children[i] < self.children[i//2]:
                    self.children[i], self.children[i//2] =  self.children[i//2],  self.children[i]
        return self
 
    def showValue(self):
        for i in self.children:
            print(i)

heap = Heap()

heap.insert(5)
heap.insert(6)
heap.insert(7)
heap.insert(8)
heap.insert(2)
heap.insert(11)
heap.insert(10)
heap.insert(1)
heap.insert(15)
heap.insert(0)
heap.insert(4)
heap.showValue()
