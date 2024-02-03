class Node(): 
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next
    
    def iterate(self):
        current = self
        while current:
            yield current.data
            current = current.next
