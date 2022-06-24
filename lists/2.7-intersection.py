# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the inter-
# secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.



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


def size(node):
    counter = 0
    while node:
        counter += 1
        node = node.next

    return counter


def last(node):
    last = None
    while node:
        last = node
        node = node.next

    return last


def indexPointer(index, node):
    while index > 0:
        index -= 1
        node = node.next

    return node


def solution(n1, n2):
    last_1 = last(n1)
    last_2 = last(n2)
    if last_1 != last_2:
        raise ValueError("lists do not intesect")

    s1 = size(n1)
    s2 = size(n2)
    if s1 > s2:
        n1 = indexPointer(s1-s2, n1)
    if s2 > s1:
        n2 = indexPointer(s2-s1, n2)

    # lists are lined up and can be checked for the intersection point
    while n1:
        if n1 == n2:
            return n1
        else:
            n1 = n1.next
            n2 = n2.next


l1 = List()
l2 = List()
l1.add(1)
l1.add(2)
l1.add(3)

l2.add(1)
l2.add(2)
l2.add(3)

n = Node(4)
l1.addNode(n)
l2.addNode(n)

assert solution(l1.head, l2.head) == n

