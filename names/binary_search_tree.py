from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if inserting root must exist
        # if value is < self.value
        if value < self.value:
            # if different keep moving
            if self.left is None:
                self.left = BinarySearchTree(value)
                # make a left node
            else:
                self.left.insert(value)
                # if >= then go right
        elif value >= self.value:
            # if not keep moving
            if self.right is None:
                self.right = BinarySearchTree(value)
                # make a new node
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # TBC
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # set up a QUEUE [allows nodes to backtrack]
        # init with root node

        # while the queue is NOT empty
            # dequeue node
            # print node.value
            # enqueue node.left, node.right
            
        storage = Queue()
        curr = self #current
        storage.enqueue(curr)
        
        while storage.len() > 0:
            curr = storage.dequeue()
            print(curr.value)
            if curr.left:
                storage.enqueue(curr.left)
            if curr.right:
                storage.enqueue(curr.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # set up a stack [node we need to backtrack to because we haven't visited both subtrees yet]
        # init with root node

        # while stack NOT empty, one thing remains that must be backtracked through
            # pop node from stacl
            # print the node.value
            # push node.left, node.right
            storage = Stack()
            curr = self #current
            storage.push(curr)
            
            while storage.len() > 0:
                curr = storage.pop() # pops node from stac1
                print(curr.value) #print node.value
                if curr.left:
                    storage.push(curr.left)
                if curr.right:
                    storage.push(curr.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is None:
            return
        print(node.value)
        node.pre_order_dft(node.left)
        node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is None:
            return
        node.post_order_dft(node.left)
        node.post_order_dft(node.right)
        print(node.value)
