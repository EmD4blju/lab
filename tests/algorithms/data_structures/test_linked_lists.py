import pytest
from algorithms.data_structures.linked_lists import LinkedList, Node


class TestNode:
    """Tests for Node class"""
    
    def test_node_creation(self):
        node = Node(5)
        assert node.value == 5
        assert node.next is None
    
    def test_node_repr(self):
        node = Node(10)
        assert repr(node) == "Node(value=10)"


class TestLinkedList:
    """Tests for LinkedList class"""
    
    def test_empty_list_initialization(self):
        ll = LinkedList()
        assert ll.head is None
        assert ll.tail is None
    
    def test_append_to_empty_list(self):
        ll = LinkedList()
        ll.append(1)
        assert ll.head is not None
        assert ll.tail is not None
        assert ll.head.value == 1
        assert ll.tail.value == 1
        assert ll.head == ll.tail
    
    def test_append_multiple_elements(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        
        # Check head and tail
        assert ll.head.value == 1
        assert ll.tail.value == 3
        
        # Traverse and verify order
        values = []
        current = ll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [1, 2, 3]
    
    def test_prepend_to_empty_list(self):
        ll = LinkedList()
        ll.prepend(1)
        assert ll.head is not None
        assert ll.tail is not None
        assert ll.head.value == 1
        assert ll.tail.value == 1
        assert ll.head == ll.tail
    
    def test_prepend_multiple_elements(self):
        ll = LinkedList()
        ll.prepend(1)
        ll.prepend(2)
        ll.prepend(3)
        
        # Check head and tail
        assert ll.head.value == 3
        assert ll.tail.value == 1
        
        # Traverse and verify order
        values = []
        current = ll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [3, 2, 1]
    
    def test_mixed_append_and_prepend(self):
        ll = LinkedList()
        ll.append(2)
        ll.prepend(1)
        ll.append(3)
        ll.prepend(0)
        
        # Traverse and verify order
        values = []
        current = ll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [0, 1, 2, 3]
    
    def test_pop_head_from_empty_list(self):
        ll = LinkedList()
        result = ll.pop_head()
        assert result is None
        assert ll.head is None
        assert ll.tail is None
    
    def test_pop_head_from_single_element_list(self):
        ll = LinkedList()
        ll.append(1)
        result = ll.pop_head()
        
        assert result == 1
        assert ll.head is None
        assert ll.tail is None
    
    def test_pop_head_multiple_times(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        
        assert ll.pop_head() == 1
        assert ll.head.value == 2
        assert ll.tail.value == 3
        
        assert ll.pop_head() == 2
        assert ll.head.value == 3
        assert ll.tail.value == 3
        
        assert ll.pop_head() == 3
        assert ll.head is None
        assert ll.tail is None
        
        assert ll.pop_head() is None
    
    def test_pop_head_updates_tail_when_empty(self):
        ll = LinkedList()
        ll.append(1)
        ll.pop_head()
        
        assert ll.head is None
        assert ll.tail is None
    
    def test_append_after_popping_all(self):
        ll = LinkedList()
        ll.append(1)
        ll.pop_head()
        ll.append(2)
        
        assert ll.head.value == 2
        assert ll.tail.value == 2
    
    def test_different_data_types(self):
        ll = LinkedList()
        ll.append("hello")
        ll.append(42)
        ll.append(3.14)
        ll.append(None)
        
        assert ll.pop_head() == "hello"
        assert ll.pop_head() == 42
        assert ll.pop_head() == 3.14
        assert ll.pop_head() is None  # This is the None we appended
        assert ll.pop_head() is None  # This is from empty list
    
    def test_delete_from_empty_list(self):
        ll = LinkedList()
        result = ll.delete(0)
        assert result is None
        assert ll.head is None
        assert ll.tail is None
    
    def test_delete_at_index_0_single_element(self):
        ll = LinkedList()
        ll.append(1)
        result = ll.delete(0)
        
        assert result == 1
        assert ll.head is None
        assert ll.tail is None
    
    def test_delete_at_index_0_multiple_elements(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        
        result = ll.delete(0)
        assert result == 1
        assert ll.head.value == 2
        assert ll.tail.value == 3
    
    def test_delete_at_last_index(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        
        result = ll.delete(2)  # Delete last element
        assert result == 3
        assert ll.head.value == 1
        assert ll.tail.value == 2
        
        # Verify list integrity
        values = []
        current = ll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [1, 2]
    
    def test_delete_middle_element(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        
        result = ll.delete(1)  # Delete second element
        assert result == 2
        
        # Verify list integrity
        values = []
        current = ll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [1, 3, 4]
        assert ll.head.value == 1
        assert ll.tail.value == 4
    
    def test_delete_multiple_elements_sequentially(self):
        ll = LinkedList()
        for i in range(5):
            ll.append(i)
        
        # Delete from middle
        assert ll.delete(2) == 2
        values = []
        current = ll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [0, 1, 3, 4]
        
        # Delete from head
        assert ll.delete(0) == 0
        values = []
        current = ll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [1, 3, 4]
        
        # Delete from tail
        assert ll.delete(2) == 4
        values = []
        current = ll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [1, 3]
    
    def test_delete_negative_index(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        
        result = ll.delete(-1)
        assert result is None
        
        # Verify list unchanged
        values = []
        current = ll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [1, 2]
    
    def test_delete_out_of_bounds_index(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        
        result = ll.delete(5)
        assert result is None
        
        # Verify list unchanged
        values = []
        current = ll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [1, 2]
    
    def test_delete_all_elements_by_index(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        
        # Delete all from head
        assert ll.delete(0) == 1
        assert ll.delete(0) == 2
        assert ll.delete(0) == 3
        
        assert ll.head is None
        assert ll.tail is None
        assert ll.delete(0) is None
    
    def test_delete_then_append(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.delete(0)
        ll.append(3)
        
        values = []
        current = ll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [2, 3]
        assert ll.head.value == 2
        assert ll.tail.value == 3


