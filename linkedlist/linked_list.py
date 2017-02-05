"""The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position <= 0:
            raise ValueError('position should be positive value.')
        current = self.head
        if self.head:
            if position == 1:
                return current
            while current.next:
                if position == 1:
                    return current
                current = current.next
                position -= 1
            if position == 1:
                return current

        else:
            return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if self.head == None:
            if position == 1:
                self.head = new_element
                new_element.next = None
            else:
                raise ValueError('position should be 1 when there is no element in the linked list.')
            return
        else:
            current = self.head
            while current.next:
                if position == 2:
                    next = current.next
                    current.next = new_element
                    new_element.next = next
                    return
                else:
                    position -= 1
                    current = current.next
            if position == 1:
                current.next = new_element
                new_element.next = None
            else:
                raise ValueError('position is larger than the number of elements in the linked list.')
            return
    
    def delete(self, value):
        """Delete the first node with a given value."""
        if self.head == None:
            return
        else:
            current = self.head
            if current.value == value:
                self.head = current.next
                return
            while current.next.next:
                if current.next.value == value:
                    nextnext = current.next.next
                    current.next = nextnext
                    return
                current = current.next
            if current.next.value == value:
                current.next = None
                return

