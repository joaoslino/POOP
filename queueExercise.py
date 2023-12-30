class Queue:

    def __init__(self):
        self.elements = []

    def insert(self, element):
        self.elements.append(element)

    def remove(self):
        if not self.is_empty():
            self.elements.pop(0)
        else:
            print("a fila esta vazia")

    def is_empty(self):
        return len(self.elements) == 0 

# testes da queue

queue=Queue() 
queue.insert(5) 
queue.insert(6) 
queue.remove() 
queue.insert(7) 
queue.remove()  
queue.remove()  
queue.remove()

print(queue.elements)