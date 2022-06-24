# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input:A -) B -) C -) 0 -) E - ) C[thesameCasearlierl
# Output:C
# Hints: #50, #69, #83, #90



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        n = Node(value)

        if self.head:
            self.tail.next = n
            self.tail = n
        else:
            self.head = n
            self.tail = n

    def addNode(self, n):

        if self.head:
            self.tail.next = n
            self.tail = n
        else:
            self.head = n
            self.tail = n


def solution(node):
    p1 = node
    p2 = node

    while p1:
        p1 = p1.next
        if p1 == p2:
            return p1
        p2 = p2.next
        if p2 is None:
            return None
        p2 = p2.next
        if p2 is None:
            return None

    return None

n = Node(5)

l = List()
l.add(1)
l.add(2)
l.addNode(n)
l.add(3)
l.add(4)

l.tail.next = n



assert solution(l.head) == n