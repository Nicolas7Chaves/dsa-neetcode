# Queues are similar to stacks, except they follow what is called a FIFO approach (First in First Out). 
# A real world example would be a line at the bank. The first person to come in the line is the first person to be served. 
# An example from the software world would be print jobs. 
# For example, if multiple people are trying to print documents, it will be handled on a first come first serve basis.


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    # Implementing this with dummy nodes would be easier!
    def __init__(self):
        self.left = self.right = None
    


# The enqueue operation adds elements to the tail of the queue until the size of the queue is reached. 
# Since adding to the end of the queue requires no shifting of the elements, this operation runs in O(1).
    def enqueue(self, val):
        newNode = ListNode(val)

        # Queue is non-empty
        if self.right:
            self.right.next = newNode
            self.right = self.right.next
        # Queue is empty
        else:
            self.left = self.right = newNode
# The dequeue operation removes elements from the front of the queue and returns that element.
    def dequeue(self):
        # Queue is empty
        if not self.left:
            return None
        
        # Remove left node and return value
        val = self.left.val
        self.left = self.left.next
        if not self.left:
            self.right = None
        return val

    def print(self):
        cur = self.left
        while cur:
            print(cur.val, ' -> ', end ="")
            cur = cur.next
        print() # new line
