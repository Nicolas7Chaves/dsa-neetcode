#Stacks are a dynamic data structure that operate on a LIFO (Last In First Out) manner. 
#The last element placed inside is the first element that comes out. 
#The stack supports three operations - push, pop, peek.

def push(self, n):
    # using the pushback function from dynamic arrays to add to the stack
    self.stack.append(n)

# Pop operation removes the last element from top of the stack, 
#which in dynamic array terms would be retrieving the last element.
#This is also an efficient O(1) operation as discussed in the previous chapters.
def pop(self):
    return self.stack.pop()


#Peek is the simplest of three. 
#It just returns, without removing, the top most element.

def peek(self):
    return self.stack[-1]