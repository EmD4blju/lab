from typing import Any, Optional


class Node:
    """Represents instances to be used in `DoubleLinkedList`
    """
    
    def __init__(self, value:Any):
        self.value = value
        self.prev:Optional[Node] = None
        self.next:Optional[Node] = None
    
    def __repr__(self):
        return f"Node(value={self.value})"
    

class DoubleLinkedList:
    """This class constitues implementation of **Double Linked List** data structure.
    """
    
    def __init__(self):
        self.head:Optional[Node] = None #~ BEGINNING
        self.tail:Optional[Node] = None #~ END
        self._len = 0
    
    def __len__(self):
        return self._len
    
    def append(self, value:Any): #~ -> O(1)
        """Creates a new `Node` with `value` & adds it as a new *tail* of the `DoubleLinkedList`.

        Args:
            value (Any): The value to be added to the `DoubleLinkedList`.
        """
        
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            old_tail = self.tail
            self.tail = new_node
            self.tail.prev = old_tail
            old_tail.next = self.tail
        
        self._len += 1
            
    def prepend(self, value:Any): #~ -> O(1)
        """Creates a new `Node` with `value` & adds it as a new *head* of the `DoubleLinkedList`.

        Args:
            value (Any): The value to be added to the `DoubleLinkedList`.
        """
        
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            self.head = new_node
            self.head.next = old_head
            old_head.prev = self.head
            
        self._len += 1
    
    def pop_head(self): #~ -> O(1)
        """Deletes and returns *head* element from `DoubleLinkedList`.
        """
        
        if not self.head: #~ If no elements
            return None
        
        if self.head == self.tail: #~ If one element
            output = self.head
            self.head = None
            self.tail = None
        else: #~ If multiple elements
            output = self.head
            self.head = output.next
            self.head.prev = None
            
        self._len -= 1
            
        return output.value
            
    def pop_tail(self): #~ -> O(1)
        """Deletes and returns *tail* element from `DoubleLinkedList`.
        """
        
        if not self.head: #~ If no elements
            return None
        
        if self.head == self.tail: #~ If one element
            output = self.tail
            self.tail = None
            self.head = None
        else: #~ If multiple elements
            output = self.tail
            self.tail = output.prev
            self.tail.next = None
        
        self._len -= 1
        
        return output.value
    
    def delete(self, pos_idx:int): #! -> O(n)
        """Deletes and returns element at `pos_idx` from `DoubleLinkedList`.

        Args:
            pos_idx (int): Index of the element to delete.
        """
            
        if not self.head: #~ If no elements
            return None
        
        if not (0 <= pos_idx < len(self)): #~ If pos_idx out of bounds
            return None
        
        if pos_idx == 0: #~ If pos_idx is at head
            return self.pop_head()
        elif pos_idx == len(self)-1: #~ If pos_idx is at tail
            return self.pop_tail()
            
        if pos_idx < len(self)//2: #~ If pos_idx is closer to head
            current_node = self.head
            while pos_idx > 0:
                current_node = current_node.next
                pos_idx -= 1
            current_node.prev.next, current_node.next.prev = current_node.next, current_node.prev
        else: #~ If pos_idx is closer to tail
            current_node = self.tail
            while pos_idx > 0:
                current_node = current_node.prev
                pos_idx -= 1
            current_node.prev.next, current_node.next.prev = current_node.next, current_node.prev
        
        self._len -= 1
        
        return current_node.value