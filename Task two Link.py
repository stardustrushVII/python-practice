class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.head = None # pushing in
        self.tail = None # missed their Switch 2 Pre-order 

    def enqueue(self, value):
        new_node = Node(value)

        if self.tail is None: # empty queue
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            raise IndexError("dequeue")

        value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None # empt q

        return value            


if __name__ == "__main__":
    q = LinkedQueue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")

    print("Dequeued:", q.dequeue())  # A
    print("Dequeued:", q.dequeue())  # B
    print("Dequeued:", q.dequeue())  # C

    try:
        q.dequeue()
    except IndexError as e:
        print ("handled Error:", e)        



