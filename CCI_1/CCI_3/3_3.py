class SetOfStacks:
    
    def __init__(self):
        self.mother = [[]]
        self.LIMIT = 5
        self.mother_stack_index = 0
    
    def push(self, data):
        le = len(self.mother[self.mother_stack_index])
        if(le < self.LIMIT):
            self.mother[self.mother_stack_index].append(data)
        if(le == self.LIMIT):
            self.mother.append([])
            self.mother_stack_index += 1
            self.mother[self.mother_stack_index].append(data)
        
    def pop(self):
        le = len(self.mother[self.mother_stack_index])
        if(le > 1):
            return self.mother[self.mother_stack_index].pop()
        if(le == 1):
            popped = self.mother[self.mother_stack_index].pop()
            del self.mother[self.mother_stack_index]
            self.mother_stack_index -= 1
            return popped
        
sos = SetOfStacks()

for i in range(12):
    sos.push(i)

for i in range(3):
    sos.pop()

print(sos.mother)