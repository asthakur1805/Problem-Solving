
class MyCircularQueue:
    
    def __init__(self,capacity):
        
        self.queue = [None]*capacity
        self.capacity = capacity
        self.count = 0
        self.front = -1
        self.rear = -1
        
    def isEmpty(self):
        
        return self.count == 0
        
    def isFull(self):
        
        return self.count == self.capacity
        
    def enQueue(self,element):
        
        if not self.isFull():
            
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = element
            self.count += 1
            return True
            
        return False
             
    def deQueue(self):
        
        if not self.isEmpty():
            
            self.front = (self.front + 1) % self.capacity
            self.queue[self.front] = None
            self.count -= 1
            return True
            
        return False
        
    def Front(self):
        
        return self.queue[(self.front+1)%self.capacity] if not self.isEmpty() else -1
        
    def Rear(self):
        
        return self.queue[self.rear] if not self.isEmpty() else -1