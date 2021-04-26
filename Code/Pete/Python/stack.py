from node import Node

class Stack:
  def __init__(self):
    self.top = None
    
  def push(self, element): # insert an element at the top (new root)
    node = Node(element, self.top)
    self.top = node
    # self.top = Node(element, self.top)
    
  def pop(self): # remove an element from the start (the root becomes the next node)
    popped_top = self.top.item
    self.top = self.top.next
    return popped_top

    
  def peek(self): # returns the element on the root node or None if there is no root
    # return self.top.item
    node = self.top
    return node.item
    
  def length(self): # return the number of elements
    length = 0
    n = self.top
    while n is not None:
      length += 1
      n = n.next
    return length
    
  def __len__(self):
    return self.length()
    
  def __str__(self):
    return str(self.top)

s = Stack()
s.push(5)
s.push(6)
print('peek', s.peek())

print('str', s)
print(len(s))


print('length', s.length()) # 2
print(s.pop()) # 6
print('peek', s.peek())
print(s.pop()) # 5

print('str', s)

print(len(s))