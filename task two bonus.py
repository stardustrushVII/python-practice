class CircularQueue:
    def __init__ (self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, item):
        if self.count == self.capacity:
            raise OverflowError("Q is too bloody full")

        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("de-Q from empty")
        
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1

        return item


if __name__ == "__main__":
    cq = CircularQueue(3)
    cq.enqueue("X")
    cq.enqueue("Y")
    cq.enqueue("Z")

    print("Queue full?", cq.is_full())  # True
    print("Dequeued:", cq.dequeue())  # Should be 'X'
    print("Dequeued:", cq.dequeue())  # Should be 'Y'
    print("Dequeued:", cq.dequeue())  # Should be 'Z'

    try:
        cq.dequeue()
    except OverflowError as e:
        print("Handled:", e)

    print("Internal state:", cq.queue)
