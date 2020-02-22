"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""



class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        cur_head = self.head #current head
        if self.head: # if head is present
            self.head = ListNode(value, None, cur_head)
            cur_head.prev = self.head
        else: #if head doesn't exist there is no tail, assign new node to head & tail
            self.head = ListNode(value)
            self.tail = self.head
        self.length += 1
            

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head: #if head is present
            cur_head = self.head
            if self.head == self.tail: #if only one node exists, make both head & tail = None
                self.head = None
                self.tail = None
                self.length -= 1
        else:
            self.head.delete()
            self.head = cur_head.next
            self.length -= 1
            
        return cur_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.tail: #if tail is present
            new_node = ListNode(value, self.tail)
            self.tail.next = new_node
            self.tail = new_node
        else: #tail isn't present means head won't exist
            self.tail = ListNode(value)
            self.head = self.tail
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        cur_tail = self.tail #current_tail
        if self.tail:
            self.length -= 1
            if self.tail == self.head:
                self.tail = None
                self.head = None
                
            else:
                self.tail = cur_tail.prev
                self.tail.next = None
                
            if cur_tail:
                return cur_tail.value
            else:
                return None

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if self.head:
            node.delete()
            cur_head = self.head
            self.head = node
            self.head.next = cur_head
            cur_head.prev = self.head 

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1
        
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        highest_value = self.head.value
        cur = self.head 
        
        while cur is not None:
            if cur.value > highest_value:
                highest_value = cur.value
            cur = cur.next
        return highest_value 