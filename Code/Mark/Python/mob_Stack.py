

class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __str__(self):
        return f'{self.item} -> {self.next}'


class Stack:
    def __init__(self):
        self.head = None

    def push(self, element):  # insert an element at the start (new root)
        # # create a new node
        # new_head = Node(element)
        # # set the next node of the new node to the head
        # new_head.next = self.head
        # # set the new node as the head
        # self.head = new_head
        
        self.head = Node(element, self.head)

    def pop(self):  # remove an element from the start (the root becomes the next node)
        # set the head as the next node of the current head
        # return the item of the old head
        if self.head == None:
            return None
        old_head = self.head
        self.head = self.head.next
        return old_head.item

    def peek(self):  # returns the element on the root node or None if there is no root
        # return the item on the head node
        if self.head == None:
            return None
        return self.head.item
    
    def is_empty(self):
        # return True if the stack is empty and false otherwise
        return self.head == None

    def length(self):  # return the number of elements
        temp_head = self.head
        count = 0
        while temp_head is not None:
            count += 1
            temp_head = temp_head.next
        return count
    
    def to_list(self):
        # convert this stack into a list
        head_list = []
        temp_head = self.head
        while temp_head is not None:
            head_list.append(temp_head.item)
            temp_head = temp_head.next
        head_list.reverse()
        return head_list

    def __str__(self):
        return str(self.head)

s = Stack()
s.push(5)
s.push(6)
s.push(7)
print(s.length())
s.push(8)
print(s.length())
print(s.to_list())



# # create nodes
# n3 = Node('pears')
# n2 = Node('bananas', n3)
# n1 = Node('apples', n2)

# # n1 -> n2 -> n3
# print(n1.item) # apples
# print(n1.next.item) # bananas
# print(n1.next.next.item) # pears
# print(n1) # ('apples',('bananas',('pears',None)))

# # iterate over the nodes
# n = n1 # temporary node we advance each iteration
# while n is not None: # stop when we run out of nodes
#   print(n.item) # prints apples, bananas, pears
#   n = n.next # advance the node to the next node
