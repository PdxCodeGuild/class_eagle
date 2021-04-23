from node import Node

class LinkedList:
  def __init__(self):
    self.root = None
  
  def append(self, element): # add the element to the end
    node = Node(element)
    if self.root is None:
      self.root = node
      return
    n = self.root
    while True:
      if n.next is None:
        n.next = node
        return
      n = n.next
  
  def insert(self, element, index): # insert the element at the given index
    i = 0
    current_node = self.root
    last_node = None
    while current_node is not None:
      if index == i:
        node = Node(element, current_node.next)
        if i == 0:
          self.root = node
        else:
          last_node.next = node
        return
      i += 1
      last_node = current_node
      current_node = current_node.next

  
  def remove(self, element): # remove the first occurrence of the element
    ...
  
  def get(self, index): # get the element at the given index (starting with 0)
    ...
  
  def find(self, element): # find the first occurrence of the element and return it
    ...
  
  def length(self): # return the length of the list
    ...

nums = LinkedList()
nums.append(5)
nums.append(6)


nums.insert(7, 0)
print(nums.root)
# print(nums) # [7, 5, 6]
# print(nums.find(5)) # 1
# nums.remove(5)
# print(nums) # [7, 6]
# print(nums.length()) # 2