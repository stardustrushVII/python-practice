class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("i really messed up")
        return self.items.pop()     
    
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("You needto dequeue, doughnut")
        return self.items.pop(0)        

# .test0
print("\n--- Queue Test ---")
q = Queue()
print("Queue empty?", q.is_empty())
q.enqueue("First")
q.enqueue("Second")
q.enqueue("Third")
print("Queue contents:", q.items)

print("Dequeued:", q.dequeue())  # First
print("Now queue:", q.items)

try:
    q.dequeue()
    q.dequeue()
    q.dequeue()  # Should raise IndexError
except IndexError as e:
    print("Handled queue error:", e)


