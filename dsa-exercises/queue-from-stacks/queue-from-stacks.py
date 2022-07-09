
class Queue_from_stack:
    def __init__(self): 
        self.queue_stack = [] 
        self.deque_stack = [] 
    
    def push(self, element): 
        self.queue_stack.append(element)

    def pop(self): 
        if not self.deque_stack: 
            while self.queue_stack: 
                self.deque_stack.append(self.queue_stack.pop())
        try: 
            return self.deque_stack.pop()
        except: 
            print("The queue is empty")
        
        return(None) 
    
    def print(self):
        print(self.deque_stack[::-1] + self.queue_stack) #bypassing queue logic just for helper print method 

queue = Queue_from_stack()

queue.print()
queue.pop()

queue.push(1)
queue.print()

queue.push(2)
queue.print()

queue.push(3)
queue.print()

queue.pop()
queue.print()

queue.push(4)
queue.print()

queue.push(5)
queue.print()

queue.pop()
queue.print()