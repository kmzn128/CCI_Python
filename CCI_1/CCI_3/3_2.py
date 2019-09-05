class MinStack:

    def __init__(self):
        self.mini = None
        self.list = []

    def push(self, item):
        if(len(self.list) == 0):
            self.mini = item
        self.list.append(item)
        if(self.mini > item):
            self.mini = item

    def pop(self):
        return self.list.pop()

    def minimum(self):
        return self.mini

ms = MinStack()
ms.push(10)
ms.push(2)
ms.push(100)
print(str(ms.minimum()))

