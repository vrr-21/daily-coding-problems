class queue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, val):
        self.stack_1.append(val)
    
    def dequeue(self):
        while len(self.stack_1) != 0:
            self.stack_2.append(self.stack_1.pop())
        if len(self.stack_2) == 0:
            return None
        else:
            t = self.stack_2.pop()
            while len(self.stack_2) != 0:
                self.stack_1.append(self.stack_2.pop())
            return t

if __name__ == '__main__':
    q = queue()
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(2)
    print(q.dequeue())
    q.enqueue(3)
    print(q.dequeue())
    