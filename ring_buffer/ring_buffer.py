from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if storage isn't full
        if self.storage.length < self.capacity:
            #adds to tail
            self.storage.add_to_tail(item)
            #updates current
            self.current = self.storage.head
            #if storage is full
        elif self.storage.length == self.capacity:
            #remove head since it is oldest value to free space
            remove_head = self.storage.head
            self.storage.remove_from_head()
            #adds item to tail and becomes newest value
            self.storage.add_to_tail(item)
            #if head set current pos to tail
            if remove_head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        start = self.current
        list_buffer_contents.append(start.value)
        #loop through nodes to append value
        if start.next:
            nxt = start.next #next
        else:
            nxt = self.storage.head
        while nxt != start:
            list_buffer_contents.append(nxt.value)
            if nxt.next:
                nxt = nxt.next
            else:
                nxt = self.storage.head
        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
