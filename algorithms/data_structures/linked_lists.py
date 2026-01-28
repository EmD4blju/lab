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
        
    
    def delete(self, pos_idx): #! -> O(n)
        if not self.head or pos_idx < 0: # If list is empty or pos_idx is negative just return None
            return None
        
        if pos_idx == 0: # If pos_idx is 0 then use O(1) pop_head() function
            return self.pop_head() 
    
        track = self.head # Tracks current element - last one will be to delete
        pre_track = None # Looks at previous element
            
        while pos_idx > 0: # When pos_idx reaches 0, track is the element to delete & pre_track is the previous element of it
            pre_track = track
            track = track.next
            if not track: # If track is None then the pos_idx is out of bounds
                return None
            pos_idx -= 1
        
        if track == self.tail: # If track is tail then set pre_track as a tail
            pre_track.next = None
            self.tail = pre_track
        else: # If track is in the middle then connect pre_track with track's next element
            pre_track.next = track.next
            track.next = None
        
        return track.value