class MyQueue:
    
    def __init__(self):
        self.a = []
        self.b = []
        
    def push(self, data):
        self.a.append(data)
    
    def pop(self):
        self._pour_to_b()
        popped = self.b.pop()
        self._pour_to_a()
        return popped
    
    def _pour_to_b(self):
        while(len(self.a) > 0):
            popped = self.a.pop()
            self.b.append(popped)
    
    def _pour_to_a(self):
        while(len(self.b) > 0):
            popped = self.b.pop()
            self.a.append(popped)
            
mq = MyQueue()

for i in range(5):
    mq.push(i)

print(mq.pop())