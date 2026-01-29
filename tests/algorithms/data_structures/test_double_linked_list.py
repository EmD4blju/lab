from algorithms.data_structures.double_linked_list import DoubleLinkedList, Node


class TestNode:
    """Tests for Node class"""
    
    def test_node_creation(self):
        """Verify node initializes with value and null next/prev pointers."""
        node = Node(5)
        assert node.value == 5
        assert node.next is None
        assert node.prev is None
    
    def test_node_repr(self):
        """Verify node string representation format."""
        node = Node(10)
        assert repr(node) == "Node(value=10)"


class TestDoubleLinkedList:
    """Tests for DoubleLinkedList class"""
    
    def test_empty_list_initialization(self):
        """Verify empty list has null head/tail and zero length."""
        dll = DoubleLinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert len(dll) == 0
    
    def test_append_to_empty_list(self):
        """Verify appending to empty list sets head and tail to same node with null pointers."""
        dll = DoubleLinkedList()
        dll.append(1)
        
        assert dll.head is not None
        assert dll.tail is not None
        assert dll.head.value == 1
        assert dll.tail.value == 1
        assert dll.head == dll.tail
        assert dll.head.prev is None
        assert dll.head.next is None
        assert len(dll) == 1
    
    def test_append_multiple_elements(self):
        """Verify appending multiple elements maintains correct head/tail and enables bidirectional traversal."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        assert dll.head.value == 1
        assert dll.tail.value == 3
        assert len(dll) == 3
        
        assert dll.head.prev is None
        assert dll.head.next.value == 2
        
        assert dll.tail.next is None
        assert dll.tail.prev.value == 2
        
        values = []
        current = dll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [1, 2, 3]
        
        values = []
        current = dll.tail
        while current:
            values.append(current.value)
            current = current.prev
        assert values == [3, 2, 1]
    
    def test_append_verifies_bidirectional_links(self):
        """Verify each node's prev and next pointers are correctly linked after appending."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        first = dll.head
        second = first.next
        third = second.next
        
        assert first.prev is None
        assert first.next == second
        
        assert second.prev == first
        assert second.next == third
        
        assert third.prev == second
        assert third.next is None
    
    def test_prepend_to_empty_list(self):
        """Verify prepending to empty list sets head and tail to same node with null pointers."""
        dll = DoubleLinkedList()
        dll.prepend(1)
        
        assert dll.head is not None
        assert dll.tail is not None
        assert dll.head.value == 1
        assert dll.tail.value == 1
        assert dll.head == dll.tail
        assert dll.head.prev is None
        assert dll.head.next is None
        assert len(dll) == 1
    
    def test_prepend_multiple_elements(self):
        """Verify prepending multiple elements maintains correct head/tail and enables bidirectional traversal."""
        dll = DoubleLinkedList()
        dll.prepend(1)
        dll.prepend(2)
        dll.prepend(3)
        
        assert dll.head.value == 3
        assert dll.tail.value == 1
        assert len(dll) == 3
        
        assert dll.head.prev is None
        assert dll.head.next.value == 2
        
        assert dll.tail.next is None
        assert dll.tail.prev.value == 2
        
        values = []
        current = dll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [3, 2, 1]
        
        values = []
        current = dll.tail
        while current:
            values.append(current.value)
            current = current.prev
        assert values == [1, 2, 3]
    
    def test_prepend_verifies_bidirectional_links(self):
        """Verify each node's prev and next pointers are correctly linked after prepending."""
        dll = DoubleLinkedList()
        dll.prepend(1)
        dll.prepend(2)
        dll.prepend(3)
        
        first = dll.head
        second = first.next
        third = second.next
        
        assert first.prev is None
        assert first.next == second
        
        assert second.prev == first
        assert second.next == third
        
        assert third.prev == second
        assert third.next is None
    
    def test_mixed_append_and_prepend(self):
        """Verify mixing append and prepend operations maintains bidirectional link integrity."""
        dll = DoubleLinkedList()
        dll.append(2)
        dll.prepend(1)
        dll.append(3)
        dll.prepend(0)
        
        assert len(dll) == 4
        
        values = []
        current = dll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [0, 1, 2, 3]
        
        values = []
        current = dll.tail
        while current:
            values.append(current.value)
            current = current.prev
        assert values == [3, 2, 1, 0]
        
        current = dll.head
        while current.next:
            assert current.next.prev == current
            current = current.next
    
    def test_pop_head_from_empty_list(self):
        """Verify popping head from empty list returns None without errors."""
        dll = DoubleLinkedList()
        result = dll.pop_head()
        
        assert result is None
        assert dll.head is None
        assert dll.tail is None
        assert len(dll) == 0
    
    def test_pop_head_from_single_element_list(self):
        """Verify popping head from single-element list clears both head and tail."""
        dll = DoubleLinkedList()
        dll.append(1)
        result = dll.pop_head()
        
        assert result == 1
        assert dll.head is None
        assert dll.tail is None
        assert len(dll) == 0
    
    def test_pop_head_from_two_element_list(self):
        """Verify popping head from two-element list leaves one node with null pointers."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        result = dll.pop_head()
        
        assert result == 1
        assert dll.head.value == 2
        assert dll.tail.value == 2
        assert dll.head == dll.tail
        assert dll.head.prev is None
        assert dll.head.next is None
        assert len(dll) == 1
    
    def test_pop_head_multiple_times(self):
        """Verify sequential pop_head operations correctly update head and maintain prev pointers."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        assert dll.pop_head() == 1
        assert dll.head.value == 2
        assert dll.head.prev is None
        assert dll.tail.value == 3
        assert len(dll) == 2
        
        assert dll.pop_head() == 2
        assert dll.head.value == 3
        assert dll.head.prev is None
        assert dll.tail.value == 3
        assert len(dll) == 1
        
        assert dll.pop_head() == 3
        assert dll.head is None
        assert dll.tail is None
        assert len(dll) == 0
        
        assert dll.pop_head() is None
    
    def test_pop_head_maintains_prev_pointer(self):
        """Verify new head's prev pointer is set to None after popping."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        dll.pop_head()
        
        assert dll.head.prev is None
        assert dll.head.value == 2
    
    def test_pop_tail_from_empty_list(self):
        """Verify popping tail from empty list returns None without errors."""
        dll = DoubleLinkedList()
        result = dll.pop_tail()
        
        assert result is None
        assert dll.head is None
        assert dll.tail is None
        assert len(dll) == 0
    
    def test_pop_tail_from_single_element_list(self):
        """Verify popping tail from single-element list clears both head and tail."""
        dll = DoubleLinkedList()
        dll.append(1)
        result = dll.pop_tail()
        
        assert result == 1
        assert dll.head is None
        assert dll.tail is None
        assert len(dll) == 0
    
    def test_pop_tail_from_two_element_list(self):
        """Verify popping tail from two-element list leaves one node with null pointers."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        result = dll.pop_tail()
        
        assert result == 2
        assert dll.head.value == 1
        assert dll.tail.value == 1
        assert dll.head == dll.tail
        assert dll.head.prev is None
        assert dll.head.next is None
        assert len(dll) == 1
    
    def test_pop_tail_multiple_times(self):
        """Verify sequential pop_tail operations correctly update tail and maintain next pointers."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        assert dll.pop_tail() == 3
        assert dll.head.value == 1
        assert dll.tail.value == 2
        assert dll.tail.next is None
        assert len(dll) == 2
        
        assert dll.pop_tail() == 2
        assert dll.head.value == 1
        assert dll.tail.value == 1
        assert dll.tail.next is None
        assert len(dll) == 1
        
        assert dll.pop_tail() == 1
        assert dll.head is None
        assert dll.tail is None
        assert len(dll) == 0
        
        assert dll.pop_tail() is None
    
    def test_pop_tail_maintains_next_pointer(self):
        """Verify new tail's next pointer is set to None after popping."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        dll.pop_tail()
        
        assert dll.tail.next is None
        assert dll.tail.value == 2
    
    def test_pop_tail_is_efficient(self):
        """Verify pop_tail is O(1) by using tail.prev pointer directly without traversal."""
        dll = DoubleLinkedList()
        for i in range(1000):
            dll.append(i)
        
        result = dll.pop_tail()
        assert result == 999
        assert dll.tail.value == 998
        assert dll.tail.next is None
        assert len(dll) == 999
    
    def test_mixed_pop_head_and_pop_tail(self):
        """Verify alternating pop_head and pop_tail operations maintain list integrity."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        dll.append(4)
        
        assert dll.pop_head() == 1
        assert len(dll) == 3
        assert dll.head.prev is None
        
        assert dll.pop_tail() == 4
        assert len(dll) == 2
        assert dll.tail.next is None
        
        assert dll.pop_head() == 2
        assert len(dll) == 1
        
        assert dll.pop_tail() == 3
        assert len(dll) == 0
        assert dll.head is None
        assert dll.tail is None
    
    def test_delete_from_empty_list(self):
        """Verify deleting from empty list returns None without errors."""
        dll = DoubleLinkedList()
        result = dll.delete(0)
        
        assert result is None
        assert dll.head is None
        assert dll.tail is None
        assert len(dll) == 0
    
    def test_delete_at_index_0_single_element(self):
        """Verify deleting only element clears both head and tail."""
        dll = DoubleLinkedList()
        dll.append(1)
        result = dll.delete(0)
        
        assert result == 1
        assert dll.head is None
        assert dll.tail is None
        assert len(dll) == 0
    
    def test_delete_at_index_0_multiple_elements(self):
        """Verify deleting head element updates head and sets new head's prev to None."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        result = dll.delete(0)
        assert result == 1
        assert dll.head.value == 2
        assert dll.head.prev is None
        assert dll.tail.value == 3
        assert len(dll) == 2
    
    def test_delete_at_last_index(self):
        """Verify deleting tail element updates tail and sets new tail's next to None."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        
        result = dll.delete(2)
        assert result == 3
        assert dll.head.value == 1
        assert dll.tail.value == 2
        assert dll.tail.next is None
        assert len(dll) == 2
        
        values = []
        current = dll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [1, 2]
        
        values = []
        current = dll.tail
        while current:
            values.append(current.value)
            current = current.prev
        assert values == [2, 1]
    
    def test_delete_middle_element(self):
        """Verify deleting middle element correctly reconnects surrounding nodes' prev and next pointers."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        dll.append(4)
        
        result = dll.delete(1)
        assert result == 2
        assert len(dll) == 3
        
        values = []
        current = dll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [1, 3, 4]
        
        values = []
        current = dll.tail
        while current:
            values.append(current.value)
            current = current.prev
        assert values == [4, 3, 1]
        
        assert dll.head.value == 1
        assert dll.head.next.value == 3
        assert dll.head.next.prev.value == 1
        assert dll.tail.value == 4
    
    def test_delete_maintains_bidirectional_links(self):
        """Verify all bidirectional links remain intact after deletion."""
        dll = DoubleLinkedList()
        for i in range(5):
            dll.append(i)
        
        dll.delete(2)
        
        current = dll.head
        while current.next:
            assert current.next.prev == current
            current = current.next
    
    def test_delete_multiple_elements_sequentially(self):
        """Verify sequential deletions from different positions maintain list integrity."""
        dll = DoubleLinkedList()
        for i in range(5):
            dll.append(i)
        
        assert dll.delete(2) == 2
        assert len(dll) == 4
        values = []
        current = dll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [0, 1, 3, 4]
        
        assert dll.delete(0) == 0
        assert len(dll) == 3
        assert dll.head.prev is None
        
        assert dll.delete(2) == 4
        assert len(dll) == 2
        assert dll.tail.next is None
        
        values = []
        current = dll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [1, 3]
    
    def test_delete_negative_index(self):
        """Verify deleting with negative index returns None and leaves list unchanged."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        
        result = dll.delete(-1)
        assert result is None
        assert len(dll) == 2
        
        values = []
        current = dll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [1, 2]
    
    def test_delete_out_of_bounds_index(self):
        """Verify deleting with out-of-bounds index returns None and leaves list unchanged."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        
        result = dll.delete(5)
        assert result is None
        assert len(dll) == 2
        
        values = []
        current = dll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [1, 2]
    
    def test_delete_all_elements_by_index(self):
        """Verify repeatedly deleting at index 0 eventually empties the list."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        assert dll.delete(0) == 1
        assert dll.delete(0) == 2
        assert dll.delete(0) == 3
        
        assert dll.head is None
        assert dll.tail is None
        assert len(dll) == 0
        assert dll.delete(0) is None
    
    def test_operations_after_deletion(self):
        """Verify list remains functional for new operations after deletion."""
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        dll.delete(1)
        
        dll.append(4)
        assert len(dll) == 3
        
        values = []
        current = dll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [1, 3, 4]
        
        values = []
        current = dll.tail
        while current:
            values.append(current.value)
            current = current.prev
        assert values == [4, 3, 1]
        
        current = dll.head
        while current.next:
            assert current.next.prev == current
            current = current.next
    
    def test_different_data_types(self):
        """Verify list handles different data types including None."""
        dll = DoubleLinkedList()
        dll.append("hello")
        dll.append(42)
        dll.append(3.14)
        dll.append(None)
        
        assert len(dll) == 4
        
        assert dll.pop_head() == "hello"
        assert dll.pop_tail() is None
        assert dll.pop_head() == 42
        assert dll.pop_head() == 3.14
        assert len(dll) == 0
    
    def test_large_list_bidirectional_integrity(self):
        """Verify bidirectional link integrity in large list with 100 elements."""
        dll = DoubleLinkedList()
        n = 100
        
        for i in range(n):
            dll.append(i)
        
        assert len(dll) == n
        
        values = []
        current = dll.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == list(range(n))
        
        values = []
        current = dll.tail
        while current:
            values.append(current.value)
            current = current.prev
        assert values == list(range(n-1, -1, -1))
        
        current = dll.head
        while current.next:
            assert current.next.prev == current
            current = current.next
    
    def test_stress_test_mixed_operations(self):
        """Verify list maintains full bidirectional integrity after complex sequence of mixed operations."""
        dll = DoubleLinkedList()
        
        for i in range(10):
            dll.append(i)
        
        dll.prepend(-1)
        dll.append(10)
        dll.pop_head()
        dll.pop_tail()
        dll.delete(5)
        
        assert len(dll) == 9
        
        current = dll.head
        count = 0
        while current:
            if current.next:
                assert current.next.prev == current
            if current.prev:
                assert current.prev.next == current
            current = current.next
            count += 1
        
        assert count == 9
        assert count == len(dll)
