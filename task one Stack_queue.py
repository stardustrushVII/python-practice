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
    
        
# .test0
if __name__ == "__main__":
    s = Stack()
    print("Is empty?", s.is_empty())
    s.push("Red Shell")
    s.push("Blue Shell")
    print("Stack after pushes:", s.items)

    print("Popped:", s.pop())
    print("Popped:", s.pop())

    try:
        print("Popped:", s.pop())  # Should raise
    except IndexError as e:
        print("Handled error:", e)

