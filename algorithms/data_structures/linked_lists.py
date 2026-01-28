class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __repr__(self):
        return f"Node(value={self.value})"
    


class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, value): #~ -> O(1)
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def prepend(self, value): #~ -> O(1)
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node    
        else:
            new_node.next = self.head
            self.head = new_node        
    
    def pop_head(self): #~ -> O(1)
        if not self.head:
            return None
        
        popped_value = self.head.value
        self.head = self.head.next
        
        if not self.head:
            self.tail = None
        
        return popped_value
        
    
    def pop_tail(self): #! -> O(n)
        if not self.head:
            return None
        
        popped_value = self.tail.value

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return popped_value
        
        track = self.head
        
        while track.next != self.tail:
            track = track.next
            
        track.next = None
        self.tail = track
        
        return popped_value
        
        
        
        
    
    def delete(self, pos_idx):
        pass